myDir = uigetdir; %gets directory
myFiles = dir(fullfile(myDir,'*.tiff'));
for k = 1:length(myFiles)
  x = 224;
  y = 224;
  baseFileName = myFiles(k).name;
  fullFileName = fullfile(myDir, baseFileName);
  img = imread(fullFileName);
  img = imresize(img,[x y],"bilinear");
  img = imnoise(img,"salt & pepper");
  %J = imrotate(img,180,'bilinear','crop');
  name = strcat('bird',int2str(k+1464),'.tiff');
  %Image_Flip = flip(img,2);
  %imwrite(Image_Flip, name);
  imwrite(img, name);
end