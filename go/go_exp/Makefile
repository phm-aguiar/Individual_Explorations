#------------------------------------------------------------------------------#
#                                  GENERICS                                    #
#------------------------------------------------------------------------------#

# Special variables
DEFAULT_GOAL: all
.DELETE_ON_ERROR: $(NAME)
.PHONY: all bonus clean fclean re

# Hide calls
export VERBOSE	=	TRUE
ifeq ($(VERBOSE),TRUE)
	HIDE = @
else
	HIDE = @
endif


#------------------------------------------------------------------------------#
#                                VARIABLES                                     #
#------------------------------------------------------------------------------#

# Compiler and flags
GO		=	go
RM		=	rm -rf

# Dir and file names
NAME	=	testes
SRCS	=	*.go

#------------------------------------------------------------------------------#
#                                 TARGETS                                      #
#------------------------------------------------------------------------------#

all:
	$(HIDE) GOOS=linux $(GO) build -o $(NAME)

fclean: 
	$(HIDE)$(RM) $(NAME)

run: all
	$(HIDE)./$(NAME)

re: fclean all
