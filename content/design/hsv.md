## HSV

## 

### Hue

For RGB, one is 0 and another is 255.

For HSL, S is 100% and L is 50%.

1. **0 => Red**
1. 40 => Orange
1. 50 => Gold
1. **60 => Yellow**
1. 75 => Lime
1. **120 => Green** 
1. 170 => Turquoise
1. **180 => Cyan**
1. 195 => Deep Sky Blue
1. 210 => Azure
1. **240 => Blue**
1. 285 => Purple
1. **300 => Magenta**
1. 330 => Pink


#1abc9c

## HSV

```python
def hsv_to_rgb(rgb, s, v):
    return [(1 - (1 - rgb[i]) * s) * v for i in range(3)]

def rgb_to_hsv(rgb):
    mn, md, mx = sorted(rgb)

    # one of the r g b is 1 at full saturation and maximum value
    v = mx

    # one of the r g b is 0 at full saturation and maximum value
    s = mx / (mx - mn)

    # (0, 1, alpha)
    # now blending 1 and alpha gives you hue
    alpha = (md - mn) / (mx - mn)
```

