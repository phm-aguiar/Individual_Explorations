package tax

import (
	"errors"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCalculateTax(t *testing.T) {
	tax, err := CalculateTax(1000.0)
	assert.Nil(t, err)
	assert.Equal(t, 10.0, tax)

	tax, err = CalculateTax(-1)
	assert.Error(t, err, "Amount cannot be negative")
	assert.Equal(t, 0.0, tax)

	tax, err = CalculateTax(0)
	assert.Nil(t, err)
	assert.Equal(t, 0.0, tax)

	tax, err = CalculateTax(20000)
	assert.Nil(t, err)
	assert.Equal(t, 20.0, tax)
}

func TestCalculateTaxAndSave(t *testing.T) {
	Repository := &TaxRepositoryMock{}
	Repository.On("SaveTax", 10.0).Return(nil)
	Repository.On("SaveTax", 0.0).Return(errors.New("error saving tax"))

	err := CalculateTaxAndSave(1000.0, Repository)
	assert.Nil(t, err)
	err = CalculateTaxAndSave(0.0, Repository)
	assert.Error(t, err, "error saving tax")

	Repository.AssertExpectations(t)
	Repository.AssertNumberOfCalls(t, "SaveTax", 2)
}
