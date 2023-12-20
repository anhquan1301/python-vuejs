<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="login-body">
    <div class="padding-login">
      <form @submit.prevent="loginUser" class="mt-3">
        <div class="wrapper bg-white mt-0">
          <div class="text-center">
            <img width="150px" src="dieucosmetics-logo.png" alt="" />
          </div>
          <div class="h4 text-secondary text-center pt-2">Đăng Nhập</div>
          <div class="form-group py-2">
            <label class="text-register">Tài khoản :</label>
            <div class="input-field-1 mt-1">
              <input
                v-model="values.username"
                type="text"
                class="input-login"
                placeholder="Nhập tài khoản"
              />
            </div>
            <div>
              <span class="text-dieucosmetics">{{ errors.username }}</span>
            </div>
          </div>
          <div class="form-group py-1 pb-2">
            <label class="text-register">Mật khẩu :</label>
            <div class="input-field-1 mt-1">
              <input
                v-model="values.password"
                :type="showPassword ? 'text' : 'password'"
                placeholder="Nhập mật khẩu"
                class="input-login"
              />
              <span
                @click="togglePasswordVisibility"
                class="bi"
                :class="{
                  'bi-eye-slash': showPassword,
                  'bi-eye': !showPassword,
                  'me-2': !showPassword
                }"
              ></span>
            </div>
            <div>
              <span class="text-dieucosmetics">{{ errors.password }}</span>
            </div>
          </div>
          <div class="d-flex justify-content-end">
            <a type="button" class="a-login" href="#" @click="handleShowFromEmail"
              >Quên mật khẩu?</a
            >
          </div>
          <div class="d-flex justify-content-center mt-2">
            <router-link to="/" class="btn btn-block text-center mx-2">Quay lại</router-link>
            <button type="submit" class="btn btn-block text-center mx-1">Đăng nhập</button>
          </div>
          <div class="text-center pt-3 text-muted">
            Bạn chưa có tài khoản?
            <router-link to="/register" class="a-login ms-1">Đăng ký</router-link>
          </div>
          <div class="mt-2">
            <router-link
              class="btn btn-google social-btn google w-75"
              to="http://localhost:8080/oauth2/authorization/google"
            >
              <img src="google-logo.png" alt="Google" />Đăng nhập bằng Google
            </router-link>
            <router-link
              class="btn btn-facebook social-btn facebook w-75"
              to="http://localhost:8080/oauth2/authorization/facebook"
            >
              <img src="fb-logo.png" alt="Facebook" />Đăng nhập bằng Facebook
            </router-link>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import Auth from '../api/Auth'

export default {
  data() {
    return {
      showPassword: false,
      showFormEmail: false,
      showOtpModal: false,
      showFormResetPass: false,
      values: {
        username: '',
        password: ''
      },
      errors: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    async loginUser() {
      // Implementation of login logic
      const handleLogin = await Auth.login(this.values)
      this.saveTokenLocally(handleLogin.data.accessToken)
      this.$router.push('/')
    },
    togglePasswordVisibility() {
      this.showPassword = !this.showPassword
    },
    handleShowFromEmail() {
      // Implementation of show form email logic
    },
    saveTokenLocally(token) {
      // Lưu token vào trình duyệt hoặc nơi khác
      // Ví dụ: Sử dụng localStorage
      localStorage.setItem('token', token)
    }
  }
}
</script>
