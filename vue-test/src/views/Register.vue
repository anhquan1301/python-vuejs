<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="login-body">
    <div class="padding-register">
      <form class="">
        <div class="wrapper-1 bg-white mt-0">
          <div class="text-center">
            <img width="150px" src="dieucosmetics-logo.png" alt="" />
          </div>
          <div class="h4 text-secondary text-center pt-2">Đăng Ký Tài Khoản</div>
          <div class="row">
            <div class="col-6">
              <div class="form-group mt-2">
                <label for="name" class="text-register">Họ và tên :</label>
                <div class="input-field-1">
                  <input
                    v-model="formData.name"
                    type="text"
                    class="input-login"
                    id="name"
                    placeholder="Nhập họ và tên"
                  />
                </div>
                <div>
                  <span class="text-danger">{{ errors.name }}</span>
                </div>
              </div>
              <div class="form-group mt-2">
                <label for="dateOfBirth" class="text-register">Ngày sinh :</label>
                <div class="input-field-1">
                  <input
                    v-model="formData.dateOfBirth"
                    type="date"
                    class="input-login"
                    id="dateOfBirth"
                  />
                </div>
                <div>
                  <span class="text-danger">{{ errors.dateOfBirth }}</span>
                </div>
              </div>
              <div class="form-group mt-2">
                <label class="text-register">Giới tính :</label>
                <div class="mt-2">
                  <div class="form-check form-check-inline">
                    <input
                      v-model="formData.gender"
                      class="form-check-input"
                      type="radio"
                      id="inlineRadio1"
                      value="false"
                    />
                    <label class="form-check-label text-register" for="inlineRadio1">Nam</label>
                  </div>
                  <div class="form-check form-check-inline">
                    <input
                      v-model="formData.gender"
                      class="form-check-input"
                      type="radio"
                      id="inlineRadio2"
                      value="true"
                    />
                    <label class="form-check-label text-register" for="inlineRadio2">Nữ</label>
                  </div>
                  <div>
                    <span class="text-danger">{{ errors.gender }}</span>
                  </div>
                </div>
              </div>
              <div class="form-group mt-2">
                <label for="email" class="text-register">Email :</label>
                <div class="input-field-1">
                  <input
                    v-model="formData.email"
                    type="text"
                    class="input-login"
                    id="email"
                    placeholder="Nhập Email"
                  />
                </div>
                <div>
                  <span v-if="showErr" class="text-danger">Email đã tồn tại</span>
                  <span v-else class="text-danger">{{ errors.email }}</span>
                </div>
              </div>
              <div class="form-group mt-2">
                <label for="phoneNumber" class="text-register">Số điện thoại :</label>
                <div class="input-field-1">
                  <input
                    v-model="formData.phoneNumber"
                    type="text"
                    class="input-login"
                    id="phoneNumber"
                    placeholder="Nhập số điện thoại"
                  />
                </div>
                <div>
                  <span class="text-danger">{{ errors.phoneNumber }}</span>
                </div>
              </div>
            </div>
            <div class="col-6">
              <div class="form-group mt-2">
                <label for="username" class="text-register">Tài khoản :</label>
                <div class="input-field-1">
                  <input
                    v-model="formData.username"
                    type="text"
                    class="input-login"
                    id="username"
                    placeholder="Nhập tài khoản"
                  />
                </div>
                <div>
                  <span v-if="showErrUsername" class="text-danger">Tài khoản đã tồn tại</span>
                  <span v-else class="text-danger">{{ errors.username }}</span>
                </div>
              </div>

              <div class="form-group mt-2">
                <label class="text-register">Mật khẩu :</label>
                <div class="input-field-1">
                  <input
                    v-model="formData.password"
                    :type="showPassword ? 'text' : 'password'"
                    placeholder="Nhập mật khẩu"
                    class="input-login"
                    name="password"
                  />
                  <span
                    @click="togglePasswordVisibility"
                    :class="showPassword ? 'bi bi-eye-slash me-2' : 'bi bi-eye me-2'"
                    role="button"
                  ></span>
                </div>
                <div>
                  <span class="text-danger">{{ errors.password }}</span>
                </div>
              </div>

              <div class="form-group mt-2">
                <label class="text-register">Xác nhận mật khẩu :</label>
                <div class="input-field-1">
                  <input
                    v-model="formData.confirmPassword"
                    :type="showPasswordConfirm ? 'text' : 'password'"
                    placeholder="Nhập mật khẩu xác nhận"
                    class="input-login"
                    name="confirmPassword"
                  />
                  <span
                    @click="togglePasswordConfirmVisibility"
                    :class="showPasswordConfirm ? 'bi bi-eye-slash me-2' : 'bi bi-eye me-2'"
                    role="button"
                  ></span>
                </div>
                <div>
                  <span class="text-danger">{{ errors.confirmPassword }}</span>
                </div>
              </div>

              <div class="form-group mt-2">
                <label for="address" class="text-register">Địa chỉ :</label>
                <div class="input-field-1">
                  <textarea
                    v-model="formData.address"
                    style="height: 96px"
                    class="input-login"
                    name="address"
                    id="address"
                    placeholder="Nhập địa chỉ"
                  ></textarea>
                </div>
                <div>
                  <span class="text-danger">{{ errors.address }}</span>
                </div>
              </div>
            </div>
            <div class="d-flex justify-content-center mt-4">
              <router-link to="/login" class="btn btn-block text-center mx-2">Hủy</router-link>
              <button
                @click.prevent="submitForm"
                type="submit"
                class="btn btn-block text-center mx-1"
              >
                Xác nhận
              </button>
            </div>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      formData: {
        name: '',
        dateOfBirth: '',
        gender: '',
        email: '',
        phoneNumber: ''
        // Các trường khác tương tự
      },
      showErr: false,
      errors: {}
    }
  },
  methods: {
    submitForm() {
      // Xử lý logic gửi form ở đây
    }
  }
}
</script>
