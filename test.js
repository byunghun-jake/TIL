function solution(S) {
  // write your code in JavaScript (Node.js 8.9.4)
  answer = 300
  for (let start_idx = 0; start_idx < S.length; start_idx++) {
    for (let end_idx = S.length - 1; end_idx > start_idx; end_idx--) {
      const alphabet = {
        a: [0, 0],
        b: [0, 0],
        c: [0, 0],
        d: [0, 0],
        e: [0, 0],
        f: [0, 0],
        g: [0, 0],
        h: [0, 0],
        i: [0, 0],
        j: [0, 0],
        k: [0, 0],
        l: [0, 0],
        m: [0, 0],
        n: [0, 0],
        o: [0, 0],
        p: [0, 0],
        q: [0, 0],
        r: [0, 0],
        s: [0, 0],
        t: [0, 0],
        u: [0, 0],
        v: [0, 0],
        w: [0, 0],
        x: [0, 0],
        y: [0, 0],
        z: [0, 0],
      }
      for (let i = start_idx; i <= end_idx; i++) {
        if (S[i].charCodeAt() < 97) {
          alphabet[S[i].toLowerCase()][1] = 1
        } else {
          alphabet[S[i].toLowerCase()][0] = 1
        }
      }
      let isBalanced = true
      Object.values(alphabet).forEach(([lower, upper]) => {
        if (lower + upper === 1) {
          isBalanced = false
        }
      })
      // console.log(S.substr(start_idx, end_idx + 1))
      // console.log(isBalanced)
      if (isBalanced && end_idx - start_idx + 1 < answer) {
        answer = end_idx - start_idx + 1
      }
    }
  }
  return answer === 300 ? -1 : answer
}

console.log(solution("aAzZ"))

{
  /* <template>
  <div>
    <!-- <form @submit="handleSubmit"> -->
    <form @submit="$emit('submit', username, password)" >
      <input id="username-input" type="text" :value="username" @input="handleChangeUsername" />
      <input id="password-input" type="password" :value="password" @input="handleChangePassword" />
      <button id="login-button" :disabled="!canSubmit">
        Submit
      </button>
    </form>
    <p>{{username}}</p>
    <p>{{password}}</p>
  </div>
</template>

<script>
export default {
  name: "LoginForm",
  emits: ["submit", "onSubmit"],
  data: function() {
    return {
      username: "",
      password: "",
    };
  },
  computed: {
    canSubmit() {
      return this.username && this.password
    }
  },
  methods: {
    handleChangeUsername(e) {
      this.username = e.target.value
    },
    handleChangePassword(e) {
      this.password = e.target.value
    },
    handleSubmit() {
      this.$emit("submit", this.username, this.password)
      this.$emit("onSubmit", this.username, this.password)
    }
  }
};
</script> */
}
