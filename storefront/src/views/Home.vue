<template>
  <div class="home">
    <div class="container">
      <div class="columns">
        <div class="column is-10 is-offset-1">
          <!-- Header Post Begin -->
          <div class="columns featured-post is-multiline">
            <div class="column is-12 post">
              <article class="columns featured">
                <div class="column is-7 post-img">
                  <img
                    src="https://cdn.emk.dev/templates/featured-image.png"
                    alt=""
                  />
                </div>
                <div class="column is-5 featured-content va">
                  <div>
                    <h3 class="heading post-category">Category Name</h3>
                    <h1 class="title post-title">Blog Posts Template</h1>
                    <p class="post-excerpt">
                      This template is based off of the official default blog
                      template created by the fine folks over at
                      <a href="https://ghost.io">Ghost</a>. If you are looking
                      for a fully featured blog platform, I highly recommend
                      checking them out!
                    </p>
                    <br />
                    <a href="#" class="button is-primary">Read More</a>
                  </div>
                </div>
              </article>
            </div>
          </div>
          <!-- Header post End -->

          <hr />

          <!-- Two Top Post Begin -->
          <div class="columns is-multiline">
            <div class="column post is-6">
              <article class="columns is-multiline">
                <div class="column is-12 post-img">
                  <img
                    src="https://cdn.emk.dev/templates/post-img.png"
                    alt="Featured Image"
                  />
                </div>
                <div class="column is-12 featured-content">
                  <h3 class="heading post-category">Category Name</h3>
                  <h1 class="title post-title">
                    Slightly Longer Blog Post Title
                  </h1>
                  <p class="post-excerpt">
                    Lorem ipsum dolor sit, amet consectetur adipisicing elit.
                    Accusamus ratione harum eaque, animi nulla tempore quis,
                    quam voluptatum.
                  </p>
                  <br />
                  <a href="#" class="button is-primary">Read More</a>
                </div>
              </article>
            </div>
            <div class="column post is-6">
              <article class="columns is-multiline">
                <div class="column is-12 post-img">
                  <img
                    src="https://cdn.emk.dev/templates/post-img.png"
                    alt="Featured Image"
                  />
                </div>
                <div class="column is-12 featured-content">
                  <h3 class="heading post-category">Category Name</h3>
                  <h1 class="title post-title">
                    Slightly Longer Blog Post Title
                  </h1>
                  <p class="post-excerpt">
                    Lorem ipsum dolor sit, amet consectetur adipisicing elit.
                    Accusamus ratione harum eaque, animi nulla tempore quis,
                    quam voluptatum.
                  </p>
                  <br />
                  <a href="#" class="button is-primary">Read More</a>
                </div>
              </article>
            </div>

            <!-- Latest Post Blog -->
            <div class="column post is-4">
            <article class="columns is-multiline">
              <div class="column is-12 post-img">
                <img src="https://cdn.emk.dev/templates/post-img.png" alt="Featured Image">
              </div>
              <div class="column is-12 featured-content ">
                <h3 class="heading post-category">Category Name</h3>
                <h1 class="title post-title">Slightly Longer Blog Post Title</h1>
                <p class="post-excerpt">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Accusamus ratione harum eaque, animi nulla tempore quis, quam voluptatum.</p>
                <br>
                <a href="#" class="button is-primary">Read More</a>
              </div>
            </article>
          </div>
          </div>
          <!-- Tow Top post End -->
        </div>
      </div>
    </div>
    <!-- <sectino class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">welcome To CodeCorp</p>
        <p class="subtitle">The Best Course Store</p>
      </div>
    </sectino> -->

    <!-- <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-1 has-text-centered">Latest products</h2>
      </div>

      <ProductBox
        v-for="product in latestProducts"
        v-bind:key="product.id"
        v-bind:product="product"
      />
    </div> -->
  </div>
</template>

<script>
import axios from "axios";
import ProductBox from "@/components/ProductBox";

export default {
  name: "Home",
  data() {
    return {
      latestProducts: [],
    };
  },
  components: {
    ProductBox,
  },
  mounted() {
    this.getLatestProducts();

    document.title = " Home | codepedia ";
  },
  methods: {
    getLatestProducts() {
      axios
        .get("/api/v1/latest-products/")
        .then((response) => {
          this.latestProducts = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
