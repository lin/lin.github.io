# Flex with Tailwind

> Always thinking in one dimensional. For two dimensional situations, using flex inside a flex.

## align-items

Just like **align items in design software**. Or `vertical-align` for text

1. if `flex flex-row` means Align Top, Align Vertical Center, Align Center
1. if `flex flex-col` means Align Left, Align Horizontal Center, Align Right
1. Tailwind: `items-start`,  `items-center`,  `items-end`

## justify-content

Just like **align text in a paragraph**, consider each 汉字 as an item. Or `text-align` for text

1. `justify-start`, Text Align Left
1. `justify-center`, Text Align Center
1. `justify-end`, Text Align Right
1. `justify-between`, Text Align Justified

## Grow Shrink & Basis

Before the remaining space is distributed. The element has a basis.


### Two and Three Equal panels

```html
<div class="h-[500px] w-screen p-12">
    <div class="flex h-full">
        <div class="basis-1/2 bg-blue-500"> <!-- Left half -->
            <!-- Content for the left half -->
        </div>
        <div class="basis-1/2 bg-red-500"> <!-- Right half -->
            <!-- Content for the right half -->
        </div>
    </div>
</div>

<div class="h-[500px] w-screen p-12">
    <div class="flex h-full">
        <div class="basis-1/3 bg-blue-500"> <!-- Left half -->
            <!-- Content for the left half -->
        </div>
        <div class="basis-1/3 bg-red-500"> <!-- Right half -->
            <!-- Content for the right half -->
        </div>
        <div class="basis-1/3 bg-green-500"> <!-- Right half -->
            <!-- Content for the right half -->
        </div>
    </div>
</div>
```
### first fix and the other two equal

```html
<div class="h-[500px] w-screen p-12">
    <div class="flex h-full">
        <div class="basis-[50px] bg-blue-500"> <!-- Left half -->
            <!-- Content for the left half -->
        </div>
        <div class="basis-[calc((100%-50px)/2)] bg-red-500"> <!-- Right half -->
            <!-- Content for the right half -->
        </div>
        <div class="basis-[calc((100%-50px)/2)] bg-green-500"> <!-- Right half -->
            <!-- Content for the right half -->
        </div>
    </div>
</div>
```

or 

```html
<div class="h-[500px] w-screen p-12">
    <div class="flex h-full">
        <div class="basis-[50px] bg-blue-500"> <!-- Left half -->
            <!-- Content for the left half -->
        </div>
        <div class="flex w-full">
             <div class="basis-1/2 bg-red-500"> <!-- Right half -->
            <!-- Content for the right half -->
            </div>
            <div class="basis-1/2 bg-green-500"> <!-- Right half -->
                <!-- Content for the right half -->
            </div>
        </div>
    </div>
</div>
```


### Two Equal panels with a gap

```html
<div class="h-[500px] w-screen p-12">
    <div class="flex h-full gap-x-12">
        <div class="basis-1/2 bg-blue-500"> <!-- Left half -->
            <!-- Content for the left half -->
        </div>
        <div class="basis-1/2 bg-red-500"> <!-- Right half -->
            <!-- Content for the right half -->
        </div>
    </div>
</div>
```
or 

```html
<div class="h-[500px] w-screen p-12">
    <div class="flex h-full space-x-12">
        <div class="basis-1/2 bg-blue-500"> <!-- Left half -->
            <!-- Content for the left half -->
        </div>
        <div class="basis-1/2 bg-red-500"> <!-- Right half -->
            <!-- Content for the right half -->
        </div>
    </div>
</div>
```



### One at one end, the other at another end

```html
<div class="h-[500px] w-screen p-12">
    <div class="flex h-full justify-between">
        <div class="w-[300px] bg-blue-500"> <!-- Left half -->
            <!-- Content for the left half -->
        </div>
        <div class="w-[300px] bg-red-500"> <!-- Right half -->
            <!-- Content for the right half -->
        </div>
    </div>
</div>
```

### equal width with 5 left and 3 right

```html
<div class="h-[500px] w-screen p-12">
    <div class="flex h-full">
        <div class="flex-1 bg-blue-100 flex flex-col gap-y-4"> <!-- Left half -->
            <!-- Content for the left half -->
            <div class="flex-1 bg-blue-400 flex"> <!-- Left half -->
                <!-- Content for the left half -->
            </div>
            <div class="flex-1 bg-blue-400 flex"> <!-- Left half -->
                <!-- Content for the left half -->
            </div>
            <div class="flex-1 bg-blue-400 flex"> <!-- Left half -->
                <!-- Content for the left half -->
            </div>
            <div class="flex-1 bg-blue-400 flex"> <!-- Left half -->
                <!-- Content for the left half -->
            </div>
            <div class="flex-1 bg-blue-400 flex"> <!-- Left half -->
                <!-- Content for the left half -->
            </div>
        </div>
        <div class="flex-1 bg-red-100 flex flex-col gap-y-4"> <!-- Left half -->
            <!-- Content for the left half -->
            <div class="flex-1 bg-red-400 flex"> <!-- Left half -->
                <!-- Content for the left half -->
            </div>
            <div class="flex-1 bg-red-400 flex"> <!-- Left half -->
                <!-- Content for the left half -->
            </div>
            <div class="flex-1 bg-red-400 flex"> <!-- Left half -->
                <!-- Content for the left half -->
            </div>
        </div>
    </div>
</div>
```

### Complex one

```html
<div class="h-[500px] w-screen p-12">
    <div class="flex h-full">
        <div class="flex-1 bg-blue-100 flex flex-col gap-y-4 items-center"> <!-- Left half -->
            <!-- Content for the left half -->
            <div class="flex-1 w-[100px] bg-blue-400 flex"> <!-- Left half -->
                <!-- Content for the left half -->
            </div>
            <div class="flex-1 w-full bg-blue-400 flex"> <!-- Left half -->
                <!-- Content for the left half -->
            </div>
            <div class="flex-1  w-[300px] bg-blue-400 flex"> <!-- Left half -->
                <!-- Content for the left half -->
            </div>
            <div class="flex-1 w-full bg-blue-400 flex"> <!-- Left half -->
                <!-- Content for the left half -->
            </div>
            <div class="flex-1  w-[400px] bg-blue-400 self-start flex "> <!-- Left half -->
                <!-- Content for the left half -->
            </div>
        </div>
        <div class="flex-1 bg-red-100 flex flex-col gap-y-4"> <!-- Left half -->
            <!-- Content for the left half -->
            <div class="flex-1 bg-red-400 flex"> <!-- Left half -->
                <!-- Content for the left half -->
            </div>
            <div class="flex-1 bg-red-400 flex"> <!-- Left half -->
                <!-- Content for the left half -->
            </div>
            <div class="flex-1 bg-red-400 flex"> <!-- Left half -->
                <!-- Content for the left half -->
            </div>
        </div>
    </div>
</div>
```