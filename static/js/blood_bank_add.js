$("form#addUser").submit(function() {
    var blood_bank_name = $('input[name="blood_bank_name"]').val().trim();
    var blood_group= $('input[name="blood_group"]').val().trim();
    var units = $('input[name="units"]').val().trim();
    var phone_no = $('input[name="phone_no"]').val().trim();
    var address = $('input[name="address"]').val().trim();
    if (blood_bank_name && blood_group && units && phone_no && address) {
        // Create Ajax Call
        $.ajax({
            url: '{% url "crud_ajax_create" %}',
            data: {
                'blood_bank_name': blood_bank_name,
                'blood_group': blood_group,
                'units': units,
                'phone_no': phone_no,
                'address': address,
              
            },
            dataType: 'json',
            success: function (data) {
                if (data.user) {
                  appendToUsrTable(data.user);
                }
            }
        });

    } else {
        alert("All fields must have a valid value.");
    }
    $('form#addUser').trigger("reset");
    return false;
});


// Delete Django Ajax Call
function deleteUser(id) {
  var action = confirm("Are you sure you want to delete this user?");
  if (action != false) {
    $.ajax({
        url: '{% url "crud_ajax_delete" %}',
        data: {
            'id': id,
        },
        dataType: 'json',
        success: function (data) {
            if (data.deleted) {
              $("#userTable #user-" + id).remove();
            }
        }
    });
  }
}


// Create Django Ajax Call
$("form#updateUser").submit(function() {
    var idInput = $('input[name="formId"]').val().trim();
    var blood_bank_name = $('input[name="formBlood_bank_name"]').val().trim();
    var blood_group = $('input[name="formBlood_group"]').val().trim();
    var units = $('input[name="formUnits"]').val().trim();
    var phone_no = $('input[name="formPhone"]').val().trim();
    var address = $('input[name="formAddress"]').val().trim();
    if (blood_bank_name &&  blood_group && units && phone_no && address) {
        // Create Ajax Call
        $.ajax({
            url: '{% url "crud_ajax_update" %}',
            data: {
                'id': idInput,
                'blood_bank_name': blood_bank_name,
                'blood_group': blood_group,
                'units': units,
                'phone_no': phone_no,
                'address': address,
            },
            dataType: 'json',
            success: function (data) {
              console.log(data)
                if (data.user) {
                  updateToUserTabel(data.user);
                  location.reload();
                }
            }
        });

    } else {
        alert("All fields must have a valid value.");
    }
    $('form#updateUser').trigger("reset");
    $('#myModal').modal('hide');
    return false;
});


// Update Django Ajax Call
function editUser(id) {
  if (id) {
    tr_id = "#user-" + id;
    blood_bank_name = $(tr_id).find(".userBlood_bank_name").text();
    blood_group = $(tr_id).find(".userBlood_group").text();
    units = $(tr_id).find(".userUnits").text();
    phone_no = $(tr_id).find(".userPhone").text();
    address = $(tr_id).find(".userAddress").text();
    console.log(true)
    $('#form-id').val(id);
    $('#form-blood_bank_name').val(blood_bank_name);
    $('#form-blood_group').val(blood_group);
    $('#form-units').val(units);
     $('#form-phone_no').val(phone_no);
    $('#form-address').val(address);
  }
}

function appendToUsrTable(user) {
  $("#userTable > tbody:last-child").append(`
        <tr id="user-${user.id}">
            <td class="userBlood_bank_name" name="name">${user.blood_bank_name}</td>
            <td class="userBlood_group" name="name">${user.blood_group}</td>
            <td class="userUnits" name="name">${user.units}</td>
            <td class="userPhone" name="name">${user.phone_no}</td>
            '<td class="userAddress" name="address">${user.address}</td>
            '<td align="center">
                <button class="btn btn-success form-control" onClick="editUser(${user.id})" data-toggle="modal" data-target="#myModal")">EDIT</button>
            </td>
            <td align="center">
                <button class="btn btn-danger form-control" onClick="deleteUser(${user.id})">DELETE</button>
            </td>
        </tr>
    `);
}

function updateToUserTabel(user){
    $("#userTable #user-" + user.id).children(".userData").each(function() {
        var attr = $(this).attr("name");
        if (attr == "name") {
          $(this).text(user.name);
        } else if (attr == "address") {
          $(this).text(user.address);
        } else {
          $(this).text(user.age);
        }
      });
}