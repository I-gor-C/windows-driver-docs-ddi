# Declarations in the aux_klib header
This header Aux_Klib contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [AuxKlibInitialize function](nf-aux-klib-auxklibinitialize.md) | The AuxKlibInitialize routine initializes the Auxiliary Kernel-Mode Library. |
| [AuxKlibGetSystemFirmwareTable function](nf-aux-klib-auxklibgetsystemfirmwaretable.md) | The AuxKlibGetSystemFirmwareTable routine retrieves the specified firmware table from the firmware table provider. |
| [AuxKlibGetImageExportDirectory function](nf-aux-klib-auxklibgetimageexportdirectory.md) | The AuxKlibGetImageExportDirectory routine returns an image module's export directory. |
| [AuxKlibQueryModuleInformation function](nf-aux-klib-auxklibquerymoduleinformation.md) | The AuxKlibQueryModuleInformation routine retrieves information about the image modules that the operating system has loaded. |
| [AuxKlibEnumerateSystemFirmwareTables function](nf-aux-klib-auxklibenumeratesystemfirmwaretables.md) | The AuxKlibEnumerateSystemFirmwareTables routine enumerates all system firmware tables of the specified type. |
| [AuxKlibGetBugCheckData function](nf-aux-klib-auxklibgetbugcheckdata.md) | The AuxKlibGetBugCheckData routine retrieves information about a bug check that has just occurred. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [AUX_MODULE_BASIC_INFO structure](ns-aux-klib--aux-module-basic-info.md) | The AUX_MODULE_BASIC_INFO structure contains basic information about a loaded image module. |
| [AUX_MODULE_EXTENDED_INFO structure](ns-aux-klib--aux-module-extended-info.md) | The AUX_MODULE_EXTENDED_INFO structure contains extended information about a loaded image module. |
| [KBUGCHECK_DATA structure](ns-aux-klib--kbugcheck-data.md) | The KBUGCHECK_DATA structure contains bug check parameters. |

This header is used in these topics:

- [kernel](..content/_kernel)
