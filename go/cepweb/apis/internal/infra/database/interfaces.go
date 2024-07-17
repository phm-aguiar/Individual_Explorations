package database

import "github.com/phm-aguiar/Individual_Explorations/go/cepweb/apis/internal/entity"

type UserInterface interface {
	Create(user *entity.User) error
	FindByEmail(email string) (*entity.User, error)
}
