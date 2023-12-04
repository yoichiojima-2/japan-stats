interface TagProps {
  onClick: () => void;
  children: React.ReactNode;
}

const Tag: React.FC<TagProps> = ({ onClick, children }) => {
  return (
    <span
      className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
      onClick={onClick}
    >
      {children}
    </span>
  );
};

export default Tag;
