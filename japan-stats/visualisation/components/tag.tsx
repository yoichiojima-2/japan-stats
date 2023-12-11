interface TagProps {
  onClick: () => void;
  children: React.ReactNode;
}

const Tag: React.FC<TagProps> = ({ onClick, children }) => {
  return (
    <span
      className="inline-block px-3 py-1 text-sm mr-2 mb-2 bg-blue-500 text-white hover:bg-blue-700 transition duration-300 ease-in-out cursor-pointer"
      onClick={onClick}
    >
      {children}
    </span>
  );
};

export default Tag;
