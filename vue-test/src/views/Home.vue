<!-- eslint-disable vue/multi-word-component-names -->
<!-- <script setup>

</script> -->

<template>
  <main>
    <div style="margin-top: 117px">
      <!-- Carousel -->
      <div id="demo" class="carousel slide" data-bs-ride="carousel">
        <!-- Indicators/dots -->
        <div class="carousel-indicators">
          <button type="button" data-bs-target="#demo" data-bs-slide-to="0" class="active"></button>
          <button type="button" data-bs-target="#demo" data-bs-slide-to="1"></button>
          <button type="button" data-bs-target="#demo" data-bs-slide-to="2"></button>
        </div>
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img
              src="dieucosmetics.png"
              alt="dieucosmetics-image"
              class="d-block"
              style="width: 100%; height: 600px; background-size: cover"
            />
          </div>
          <div class="carousel-item">
            <img
              src="https://theme.hstatic.net/1000373343/1000671881/14/slideshow_1.jpg?v=81"
              alt=""
              class="d-block"
              style="width: 100%; height: 600px; background-size: cover"
            />
          </div>
          <div class="carousel-item">
            <img
              src="https://theme.hstatic.net/1000373343/1000671881/14/slideshow_3.jpg?v=81"
              alt=""
              class="d-block"
              style="width: 100%; height: 600px; background-size: cover"
            />
          </div>
        </div>
        <button
          class="carousel-control-prev"
          type="button"
          data-bs-target="#demo"
          data-bs-slide="prev"
        >
          <span class="carousel-control-prev-icon"></span>
        </button>
        <button
          class="carousel-control-next"
          type="button"
          data-bs-target="#demo"
          data-bs-slide="next"
        >
          <span class="carousel-control-next-icon"></span>
        </button>
      </div>
    </div>
    <section class="service-policy-area section-space container">
      <div class="container mt-5">
        <div class="d-flex">
          <div v-for="(image, index) in images" :key="index" class="col-lg-2 mx-4 px-0">
            <a :href="image.link">
              <img
                :src="image.src"
                class="d-block w-100 h-100 img-producer"
                :alt="'Brand Image ' + (index + 1)"
              />
            </a>
          </div>
        </div>
      </div>
    </section>
    <section class="service-policy-area section-space container">
      <div>
        <h2 class="text-center bg-home text-secondary py-3">SẢN PHẨM KHUYẾN MÃI</h2>
      </div>
      <div class="container">
        <div
          id="carouselExampleControls"
          class="carousel carousel-dark slide"
          data-bs-ride="carousel"
        >
          <div class="carousel-inner">
            <div class="carousel-item active">
              <div class="row d-flex justify-content-center mt-3">
                <div class="col-lg-2 mx-4 px-0">
                  <div class="card-1">
                    <img class="card-img-top" alt="..." />
                    <div class="card-body">
                      <div></div>
                      <p>
                        <span class="text-decoration-line-through"> </span>
                        <span class="text-danger fs-6 float-end fw-bold"> </span>
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="carousel-item">
              <div class="row d-flex justify-content-center mt-3">
                <div class="col-lg-2 mx-4 px-0">
                  <div class="card-1">
                    <img class="card-img-top" alt="..." />
                    <div class="card-body">
                      <div></div>
                      <p>
                        <span class="text-decoration-line-through"> </span>
                        <span class="text-danger fs-6 float-end fw-bold"> </span>
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <button
            class="carousel-control-prev"
            type="button"
            data-bs-target="#carouselExampleControls"
            data-bs-slide="prev"
          >
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button
            class="carousel-control-next"
            type="button"
            data-bs-target="#carouselExampleControls"
            data-bs-slide="next"
          >
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
      </div>
    </section>
    <hr class="mx-5 hr-dieucosmetics" />
    <div class="container px-0 mt-5">
      <div class="row mx-0 mt-2 mb-5 ms-5">
        <div class="col-4">
          <h4 style="color: GrayText; margin-top: 20px">
            Tất cả đều là Mỹ phẩm Thảo dược và nó được bào chế, sử dụng các thành phần mỹ phẩm thảo
            dược được phép khác nhau, là các sản phẩm 100% từ Thảo dược nguyên chất và an toàn.
          </h4>
        </div>
        <div class="col-4">
          <img
            class="w-100 h-100 shadow"
            src="https://file.hstatic.net/200000259653/file/1_b43b5110a90346c6b860cd09ab127476.jpg"
            alt=""
          />
        </div>
        <div class="col-4">
          <h4 style="text-align: center; color: GrayText; padding-top: 20px">
            KEM DƯỠNG MẶT THẢO DƯỢC
          </h4>
          <h6 style="color: black; line-height: 2; font-family: 'Cormorant Infant', 'serif'">
            Chứa thành phần dưỡng chất của Aloe Vera, Vitamin E và Vitamin B5, do đó nó làm dịu và
            làm mềm làn da của bạn và mang lại cho bạn một làn da sáng tự nhiên trên khuôn mặt của
            bạn.
          </h6>
        </div>
      </div>
      <div class="shadow-cosmetics-1">
        <div class="row mx-0 bg-home text-white">
          <div class="row container mx-0 px-0">
            <div class="column col-6 px-0 figure" id="zoomIn">
              <img
                class="w-100 h-100"
                src="https://theme.hstatic.net/200000384051/1000742014/14/home_about_img.jpg?v=1609"
              />
            </div>
            <div class="col-6 mt-2">
              <h3 style="text-align: center; color: GrayText; padding-top: 30px">
                BST MỸ PHẨM CHÍNH HÃNG DieuCosmetics
              </h3>
              <h6
                style="
                  color: black;
                  line-height: 2;
                  padding-top: 20px;
                  padding-left: 30px;
                  padding-right: 30px;
                  font-family: 'Cormorant Infant', 'serif';
                "
              >
                Hướng đến trang điểm cá nhân với thiết kế đơn giản, tiện dụng, nhỏ gọn, tiện lợi
                mang theo, chất lượng tốt, giá rẻ. Với các thành phần dưỡng chất đến từ collagen cá,
                tinh dầu bơ, mật ong, tinh chất các loài hoa: hoa anh đào, hoa citron,… bột ngọc
                trai, vitamin E, chiết xuất trà xanh, tinh dầu bơ hạt mỡ,….Tích hợp thành phần chống
                nắng, dưỡng da, kiềm dầu, cân bằng độ ẩm, hạn chế các hoạt động của mụn và ổ viêm
                gây mụn, se khít lỗ chân lông, tái tạo lớp biểu bì.
              </h6>
            </div>
          </div>
        </div>
        <div class="row mx-0">
          <div class="row container mx-0 px-0">
            <div class="col-6 mt-2 px-0">
              <h3 style="text-align: center; color: GrayText; padding-top: 30px">
                PHÂN PHỐI ĐA DẠNG CÁC DÒNG SẢN PHẨM
              </h3>
              <h6
                style="
                  color: black;
                  line-height: 2;
                  padding-top: 10px;
                  padding-left: 30px;
                  padding-right: 30px;
                  font-family: 'Cormorant Infant', 'serif';
                "
              >
                DieuCosmetics hiện đang phân phối các dòng mỹ phẩm trang điểm: Kem lót, kem nền,
                phấn nước cushion, kem che khuyết điểm, phấn phủ, bút kẻ chân mày, phấn má hồng, chì
                kẻ mắt, mascara, phấn mắt, kem chống nắng, son môi. Một vài sản phẩm skin care:
                Serum dưỡng dài mi, các sản phẩm nước tẩy trang (dạng nước, dạng dầu, dạng kem), sữa
                rửa mặt. Dịu nhẹ, thích hợp với da nhạy cảm, mụn dầu của các cô gái Á Đông. Giúp bạn
                thoải mái trang điểm mà không lo đổ dầu, nổi mụn hay kích ứng, lâu trôi.
              </h6>
            </div>
            <div class="col-6 px-0 column figure" id="zoomIn">
              <img
                class="w-100 h-100"
                src="https://file.hstatic.net/200000259653/file/3_c36448acd2764e8a8d49c4fd740a8523.jpg"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
    <hr class="mx-5 hr-dieucosmetics mt-5" />
    <div class="container mt-5 bg-home py-5 mb-5">
      <div class="row">
        <div class="col-lg-3 col-md-6 col-sm-6">
          <div class="service-policy-item">
            <div class="icons">
              <img
                src="https://demo.hasthemes.com/floda-preview/floda/assets/img/icon/free_shipping.png"
                alt=""
              />
            </div>
            <div class="policy-terms">
              <h5>Miễn Phí Giao Hàng</h5>
              <p>Miễn phí giao hàng toàn quốc</p>
            </div>
          </div>
        </div>
        <div class="col-lg-3 col-md-6 col-sm-6">
          <div class="service-policy-item">
            <div class="icons">
              <img
                src="https://demo.hasthemes.com/floda-preview/floda/assets/img/icon/support247.png"
                alt=""
              />
            </div>
            <div class="policy-terms">
              <h5>Hỗ Trợ 24/7</h5>
              <p>Hỗ trợ 24h trong 1 ngày</p>
            </div>
          </div>
        </div>
        <div class="col-lg-3 col-md-6 col-sm-6">
          <div class="service-policy-item">
            <div class="icons">
              <img
                src="https://demo.hasthemes.com/floda-preview/floda/assets/img/icon/money_back.png"
                alt=""
              />
            </div>
            <div class="policy-terms">
              <h5>Hoàn Trả Lại Tiền</h5>
              <p>Hoàn trả lại tiền trong vòng 30 ngày</p>
            </div>
          </div>
        </div>
        <div class="col-lg-3 col-md-6 col-sm-6">
          <div class="service-policy-item">
            <div class="icons">
              <img
                src="https://demo.hasthemes.com/floda-preview/floda/assets/img/icon/promotions.png"
                alt=""
              />
            </div>
            <div class="policy-terms">
              <h5>Giảm Giá Đặt Hàng</h5>
              <p>Giảm giá 5% trên mỗi đơn hàng</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>
<script>
export default {
  data() {
    return {
      images: [
        {
          link: '',
          src: 'https://theme.hstatic.net/200000384051/1000742014/14/home_brand_image_1.jpg?v=1609'
        },
        {
          link: '',
          src: 'https://theme.hstatic.net/200000384051/1000742014/14/home_brand_image_2.jpg?v=1609'
        },
        {
          link: '',
          src: 'https://theme.hstatic.net/200000384051/1000742014/14/home_brand_image_3.jpg?v=1609'
        },
        {
          link: '',
          src: 'https://theme.hstatic.net/200000384051/1000742014/14/home_brand_image_4.jpg?v=1609'
        },
        {
          link: '',
          src: 'https://theme.hstatic.net/200000384051/1000742014/14/home_brand_image_7.jpg?v=1609'
        }
      ]
    }
  },
  props: {
    productSaleList: Array
  },
  methods: {
    handleDetailProduct(id) {
      // Xử lý sự kiện khi click vào sản phẩm
      console.log('Detail product ID:', id)
    }
  }
}
</script>
