import os
import _winreg as wreg

__author__ = 'G4l_B1t'

"""
Creating artifacts searched by malware using this script may repel potential attackers.
Feel free to use it **at your own risk**.
"""


def create_file(f, t):
    """
    create file or folder if it doesn't exist
    """
    print "\t+ creating {0}".format(f)
    try:
        if os.path.exists(f):
            print "\t+ {0} already exists!\n".format(f)
        else:
            if t == "file":
                open(f, 'w')
            elif t == "folder":
                os.makedirs(f)
            print "\t+ {0} was created!\n".format(f)

    except Exception as e:
        error_on_create(f, e)


def create_reg_key(hive, k):
    """
    create registry key
    currently supports only 32bit machines
    """
    print "\t+ creating {0}".format("HKLM", "\\", k)
    try:
        wreg.CreateKey(hive, k)
        print "\t+ {0} was created!\n".format("HKLM", "\\", k)
    except Exception as e:
        error_on_create(k, e)


def create_reg_val(k, v_name, v_data):
    """
    create and set registry value
    currently supports only 32bit machines and HKLM registry keys and values
    """
    print "\t+ creating {0}".format(k, "\\", v_name)
    try:
        kh = wreg.OpenKey(wreg.HKEY_LOCAL_MACHINE, k, 0, wreg.KEY_ALL_ACCESS)
        wreg.SetValueEx(kh, v_name, 0, wreg.REG_SZ, v_data)
        print "\t+ {0} was created!\n".format(k, "\\", v_name)
    except Exception as e:
        error_on_create(k + "\\" + v_name, e)


def error_on_create(i, e):
    print "\t+ error creating {0}\n\t+ Error was: {1}\n".format(i, e)


if __name__ == '__main__':

    dir_list = [
        "C:\\program files\\VMware",
        "C:\\program files\\oracle\\virtualbox guest additions",
        "C:\\Program Files\\Malware Bytes"
    ]

    file_list = [
        "C:\\Program Files\\Malware Bytes\\mbam.exe",
        "C:\\Program Files\\Malware Bytes\\mbae.exe",
        "C:\\WINDOWS\\system32\\drivers\\vmmouse.sys",
        "C:\\WINDOWS\\system32\\drivers\\vmhgfs.sys",
        "C:\\WINDOWS\\system32\\drivers\\VBoxMouse.sys",
        "C:\\WINDOWS\\system32\\drivers\\VBoxGuest.sys",
        "C:\\WINDOWS\\system32\\drivers\\VBoxSF.sys",
        "C:\\WINDOWS\\system32\\drivers\\VBoxVideo.sys",
        "C:\\WINDOWS\\system32\\vboxdisp.dll",
        "C:\\WINDOWS\\system32\\vboxhook.dll",
        "C:\\WINDOWS\\system32\\vboxmrxnp.dll",
        "C:\\WINDOWS\\system32\\vboxogl.dll",
        "C:\\WINDOWS\\system32\\vboxoglarrayspu.dll",
        "C:\\WINDOWS\\system32\\vboxoglcrutil.dll",
        "C:\\WINDOWS\\system32\\vboxoglerrorspu.dll",
        "C:\\WINDOWS\\system32\\vboxoglfeedbackspu.dll",
        "C:\\WINDOWS\\system32\\vboxoglpackspu.dll",
        "C:\\WINDOWS\\system32\\vboxoglpassthroughspu.dll",
        "C:\\WINDOWS\\system32\\vboxservice.exe",
        "C:\\WINDOWS\\system32\\vboxtray.exe",
        "C:\\WINDOWS\\system32\\VBoxControl.exe"
    ]

    key_list = [
        [wreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Wireshark"],
        [wreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\ESET"],
        [wreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\AVAST"],
        [wreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\VMware, Inc.\\VMware Tools"],
        [wreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Oracle\\VirtualBox Guest Additions"],
        [wreg.HKEY_LOCAL_MACHINE, "HARDWARE\\ACPI\\DSDT\\VBOX__"],
        [wreg.HKEY_LOCAL_MACHINE, "HARDWARE\\ACPI\\FADT\\VBOX__"],
        [wreg.HKEY_LOCAL_MACHINE, "HARDWARE\\ACPI\\RSDT\\VBOX__"],
        [wreg.HKEY_LOCAL_MACHINE, "SYSTEM\\ControlSet001\\Services\\VBoxGuest"],
        [wreg.HKEY_LOCAL_MACHINE, "SYSTEM\\ControlSet001\\Services\\VBoxMouse"],
        [wreg.HKEY_LOCAL_MACHINE, "SYSTEM\\ControlSet001\\Services\\VBoxService"],
        [wreg.HKEY_LOCAL_MACHINE, "SYSTEM\\ControlSet001\\Services\\VBoxSF"],
        [wreg.HKEY_LOCAL_MACHINE, "SYSTEM\\ControlSet001\\Services\\VBoxVideo"],
        [wreg.HKEY_CURRENT_USER, "SOFTWARE\\Wine"],
    ]

    key_value_list = [
        ["HARDWARE\\DESCRIPTION\\System", "SystemBiosVersion", "QEMU"],
        ["HARDWARE\\DEVICEMAP\\Scsi\\Scsi Port 2\\Scsi Bus 0\\Target Id 0\\Logical Unit Id 0", "Identifier", "VMWARE"],
        ["HARDWARE\\Description\\System", "VideoBiosVersion", "VIRTUALBOX"],
        ["HARDWARE\\DESCRIPTION\\System", "SystemBiosDate", "06/23/99"]
    ]

    print "\ninitiating vaccination..."

    print "\n+ Phase A: creating folders\n"
    for dir_item in dir_list:
        create_file(dir_item, "folder")

    print "\n+ Phase B: creating files\n"
    for file_item in file_list:
        create_file(file_item, "file")

    print "\n+ Phase C: creating registry keys\n"

    for reg_key in key_list:
        create_reg_key(reg_key[0], reg_key[1])

    print "\n+ Phase D: creating registry values\n"

    for reg_value in key_value_list:
        create_reg_val(reg_value[0], reg_value[1], reg_value[2])

    print "\n||=====()))))))))))))----->\nyou are now vaccinated!"
