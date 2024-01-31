original_image = imread("mickey-1.png")

%read the output variable from the file
c_output_variable = fileread('c_output.txt');
haskell_output_variable = fileread('haskell_output.txt');
prolog_output_variable  =fileread('prolog_output.txt');

%convert the numeric array to unsigned char
c_output_array = uint8(str2num(c_output_variable));
haskell_output_array = uint8(str2num(haskell_output_variable));
prolog_output_array= uint8(str2num(prolog_output_variable)); 


%resize to a orginal size(adjust based on your data format)
c_resized_matrix = reshape(c_output_array, 256, 256);
haskell_resized_matrix = reshape(haskell_output_array, 256, 256);
prolog_resized_matrix = reshape(prolog_output_array, 256, 256);


%display the resized matrix as an image

figure;
subplot(2,2,1);
imshow(original_image);
title('Original Image');

subplot(2,2,2);
imshow(c_resized_matrix);
title('Black & White Image from C');


subplot(2,2,3)
imshow(haskell_resized_matrix);
title('Color Fliped Image using Haskell Program');

subplot(2,2,4)
imshow(prolog_resized_matrix);
title('Rotate Image using Prolog Program');
