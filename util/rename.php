<?php

foreach(glob('style/icon/32/*.png') as $file) {
  $path = dirname($file);
  $name = strtolower(basename($file));
  $name = preg_replace('/[^0-9a-z]{3,}/', '-', $name);
  $name = preg_replace('/\s+/', '-', $name);
  $name = preg_replace('/[^0-9a-z\.\-]/', '', $name);
  rename($file, $path.'/'.$name);
}