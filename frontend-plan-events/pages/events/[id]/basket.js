import { useRouter } from "next/router";
import MainContainer from "../../../componets/MainContainer";
import Product from "../../../componets/basket/Product.js"
import { useHttp } from "../../../hooks/http.hook";
import styles from "../../../styles/events/Basket.module.css";
import { useState } from "react";
import ProductForm from "../../../componets/basket/ProductForm";

export default function Basket({ user }) {
  let [products, setProducts] = useState([
    {name:"Арбуз", price:"40р за кг", quantity:"10кг"},
    {name:"Торт", price:"1000р за кг", quantity:"1.3кг"},
    {name:"Овощи", price:"400р за кг", quantity:"3кг"},
    {name:"Мясо", price:"800р за кг", quantity:"6кг"},
  ]);

  let [product, setProduct] = useState({name:"", price:"", quantity:""});
  let [add_product_mode, set_add_product_mode] = useState(false);

  let show_product_form = () => set_add_product_mode(!add_product_mode);

  let change_product = (event) => {
    console.log(event.target.value);
    product[event.target.id] = event.target.value;
    setProduct(product);
  }  

  let add_product = () => {
    if(!(product.name && product.quantity && product.price))return;
    products.push(product);
    setProducts(products);
    setProduct({name:"", price:"", quantity:""});
    set_add_product_mode(false);
  }

  const { query } = useRouter();
  const {loading, request, error, clearError} = useHttp()

  const check = async () => {
    try {
      const data = await request("/auth", "GET");
      console.log(data);
    } catch (e) {
      console.error(e);
    }
  };

  return (
    <MainContainer keywords={user.name}>
      <div className={styles.root}>
        <div className={styles.content}>
          <div className={styles.head}>
            <h2>Список</h2>
          </div>
          {add_product_mode ? 
            <ProductForm change_product={change_product}></ProductForm>
            :
            <div className={styles.list}>
              {products.map((item) => {
                return (
                  <Product item={item}></Product>
                );
              })}
            </div>
          }
          
          <div className={styles.button}>
            {add_product_mode ? 
              <button onClick={add_product}>Добавить</button>
              :
              <button onClick={show_product_form}>Добавить в список</button>
            }
          </div>
        </div>
      </div>
    </MainContainer>
  );
}

export async function getServerSideProps({ params }) {
  const response = await fetch(
    `https://jsonplaceholder.typicode.com/users/${params.id}`
  );
  const user = await response.json();
  return {
    props: { user }, // will be passed to the page component as props
  };
}
