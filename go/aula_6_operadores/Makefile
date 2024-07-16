#------------------------------------------------------------------------------#
#                                  GENERICS                                    #
#------------------------------------------------------------------------------#

# Special variables
DEFAULT_GOAL: all
.DELETE_ON_ERROR: $(NAME)
.PHONY: all fclean re
# 'HIDE = @' will hide all terminal output from Make
HIDE =


#------------------------------------------------------------------------------#
#                                VARIABLES                                     #
#------------------------------------------------------------------------------#

# Compiler and flags
GO		=	go
RM		=	rm -f

# Output file name
NAME	=	operator

# Sources are all .c files
SRCDIR	=	src/
SRCS	=	$(wildcard $(SRCDIR)*.go)



#------------------------------------------------------------------------------#
#                                 TARGETS                                      #
#------------------------------------------------------------------------------#

all: $(NAME)

# Compiles the program
$(NAME): $(SRCS)
	$(HIDE)$(GO) build -o $(NAME) $(SRCS)

fclean: clean
	$(HIDE)$(RM) $(NAME)

run: all
	$(HIDE)./$(NAME)

re: fclean all
