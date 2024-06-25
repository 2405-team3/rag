import { useState } from "react";
import * as service from "../services/service";

export default function UploadForm() {
  const [file, setFile] = useState<File | null>(null);

  function handleChange(e: React.FormEvent<HTMLInputElement>) {
    const target = e.target as HTMLInputElement & {
      files: FileList;
    };
    setFile(target.files[0]);
  }

  async function handleSubmit(e: React.SyntheticEvent) {
    e.preventDefault();
    if (!file) return;

    const formData = new FormData();
    formData.set("file", file);
    await service.uploadFile(formData);
  }

  return (
    <form action="" onSubmit={handleSubmit}>
      <h2>Upload a Document</h2>
      <label htmlFor="document">Document</label>
      <input
        required
        type="file"
        name="document"
        id="document"
        onChange={handleChange}
      />
      <button type="submit">Upload</button>
    </form>
  );
}
