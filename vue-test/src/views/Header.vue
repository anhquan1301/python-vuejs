<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <header>
    <nav class="header-fixed border-bottom border-color">
      <div
        :style="{ backgroundColor: '#fff' }"
        class="d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-3 header-shadow"
      >
        <router-link
          to="/"
          class="d-flex align-items-center ms-5 col-md-3 mb-2 mb-md-0 text-dark text-decoration-none"
          :style="{ marginRight: '-220px' }"
        >
          <img :width="150" src="/dieucosmetics-logo.png" alt="dieucosmetics-logo" />
        </router-link>
        <ul class="nav col-12 col-md-auto mb-2 justify-content-center mb-md-0">
          <li>
            <router-link to="/" class="nav-link px-4 text-secondary text-hover">
              TRANG CHỦ
            </router-link>
          </li>
          <li>
            <a href="#" class="nav-link px-4 text-secondary text-hover"> GIỚI THIỆU </a>
          </li>
          <li>
            <router-link to="/product" class="nav-link px-4 text-secondary text-hover">
              SẢN PHẨM
            </router-link>
          </li>
          <li>
            <a href="#" class="nav-link px-4 text-secondary text-hover"> KHUYẾN MÃI </a>
          </li>
          <li>
            <a href="#" class="nav-link px-4 text-secondary text-hover"> HỖ TRỢ </a>
          </li>
        </ul>

        <div class="fs-5 search-container">
          <i class="bi bi-search">
            <span class="ms-2 position-absolute" :style="{ bottom: '3px' }">|</span>
          </i>
          <input
            type="text"
            class="form-control search-product"
            v-model="searchInput"
            @keydown="handleSearchProduct"
            @input="handleSearch"
            placeholder="Tìm kiếm sản phẩm"
          />
        </div>
        <div class="me-5 fs-4">
          <div class="float-start">
            <template v-if="token === null">
              <router-link to="/login" type="button" class="ms-5 bi bi-person"></router-link>
            </template>
            <template v-else>
              <div class="ms-5">
                <div class="dropdown">
                  <a
                    class="dropdown-toggle d-flex align-items-center hidden-arrow"
                    id="navbarDropdownMenuAvatar"
                    role="button"
                    data-bs-toggle="dropdown"
                    aria-expanded="false"
                  >
                    <div class="fs-6" :style="{ width: '40px', height: '40px' }">
                      <img
                        :src="avatar === '' ? avatarDetail : avatar"
                        class="rounded-circle border border-2 border-color"
                        alt="avatar"
                        width="100%"
                        height="100%"
                      />
                    </div>
                  </a>
                  <ul class="dropdown-menu p-0" aria-labelledby="navbarDropdownMenuAvatar">
                    <li>
                      <router-link to="/customer/detail" class="dropdown-item button-buy">
                        Thông tin cá nhân
                      </router-link>
                    </li>
                    <li>
                      <button @click="handleLogout" class="dropdown-item button-buy" href="#">
                        Đăng xuất
                      </button>
                    </li>
                  </ul>
                </div>
              </div>
            </template>
          </div>
          <div class="float-end cart-container">
            <router-link to="/cart" class="ms-3 me-5 pe-5 bi bi-cart3"></router-link>
            <span class="me-5 pe-5 cart-number">{{ iconQuantity === 0 ? '' : iconQuantity }}</span>
          </div>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  data() {
    return {
      searchInput: '',
      token: localStorage.getItem('token'), // Replace with your logic for token
      avatar: '', // Replace with your logic for avatar
      avatarDetail: '', // Replace with your default avatar URL
      iconQuantity: 0 // Replace with your logic for cart quantity
    }
  },
  methods: {
    handleSearchProduct() {
      // Implement your search logic here
    },
    handleSearch() {
      // Implement your search logic here
    },
    handleLogout() {
      localStorage.clear()
      this.$router.push('/')
    }
  }
}
</script>
