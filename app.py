def main():
    st.title("Image Captioning with ViT-GPT2")
    st.write("Upload an image and get a caption!")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)

            # Perform prediction
            preds = predict_step([uploaded_file])

            # Display captions
            st.subheader("Predicted Caption:")
            for pred in preds:
                st.write(pred)

        except Exception as e:
            st.error(f"An error occurred: {e}")
