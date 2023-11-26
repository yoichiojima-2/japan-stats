import Papa from 'papaparse';

const parse_csv = async (filePath) => {
    const response = await fetch(filePath);
    const reader = response.body.getReader();
    const result = await reader.read();
    const decoder = new TextDecoder('utf-8');
    const csv = decoder.decode(result.value);

    return new Promise((resolve, reject) => {
        Papa.parse(
            csv, {
                header: true,
                complete: (results) => resolve(results.data),
                error: (error) => reject(error),
            }
        );
    });
};

export default parse_csv;