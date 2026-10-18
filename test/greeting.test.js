const { test } = require('node:test');
const assert = require('node:assert/strict');
const { greeting } = require('../src/greeting');

test('нэрээр зөв мэндчилгээ үүсгэнэ', () => {
  assert.equal(greeting('Оюутан'), 'Сайн байна уу, Оюутан!');
});

test('хоосон нэрийн үед мэндчилгээ үүсгэнэ', () => {
  assert.equal(greeting(''), 'Сайн байна уу, !');
});
