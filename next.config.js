module.exports = {
  async rewrites() {
    return [
      {
        source: '/fonts',
        destination: '/fonts.html',
      },
    ]
  },
}