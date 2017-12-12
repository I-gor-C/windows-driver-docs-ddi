---
UID: NS.PEPFX._PEP_ACPI_REGISTER_DEVICE
title: _PEP_ACPI_REGISTER_DEVICE
author: windows-driver-content
description: The PEP_ACPI_REGISTER_DEVICE structure contains registration information about a device for which the platform extension plug-in (PEP) is to provide ACPI services.
old-location: kernel\pep_acpi_register_device.htm
old-project: kernel
ms.assetid: 96FB6959-1583-42E0-9851-A09AE0CB73DB
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: _PEP_ACPI_REGISTER_DEVICE, *PPEP_ACPI_REGISTER_DEVICE, PEP_ACPI_REGISTER_DEVICE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_ACPI_REGISTER_DEVICE
req.alt-loc: pepfx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
---

# _PEP_ACPI_REGISTER_DEVICE structure



## -description
The <b>PEP_ACPI_REGISTER_DEVICE</b> structure contains registration information about a device for which the platform extension plug-in (PEP) is to provide ACPI services.



## -syntax

````
typedef struct _PEP_ACPI_REGISTER_DEVICE {
  PANSI_STRING AcpiDeviceName;
  ULONG        InputFlags;
  POHANDLE     KernelHandle;
  PEPHANDLE    DeviceHandle;
  ULONG        OutputFlags;
} PEP_ACPI_REGISTER_DEVICE, *PPEP_ACPI_REGISTER_DEVICE;
````


## -struct-fields

### -field AcpiDeviceName

[in] An <a href="kernel.ansi_string">ANSI_STRING</a> structure that contains the fully qualified BIOS name for the device. The same name was previously supplied as an input value in the <a href="kernel.pep_acpi_prepare_device">PEP_ACPI_PREPARE_DEVICE</a> notification for the device. This name specifies the path and name of the device in the ACPI namespace. For more information, see <a href="https://msdn.microsoft.com/fe0553df-a5b9-46c4-8e1d-8b89a7d4ad67">Enumerating Child Devices and Control Methods</a>.


### -field InputFlags

[in] A set of input flags. No flags are currently defined for this member, which is always set to PEP_ACPI_REGISTER_DEVICE_INPUT_FLAG_NONE (0x0).


### -field KernelHandle

[in] A POHANDLE value that represents the registration of the device with the Windows <a href="kernel.power_management_framework__pofx__routines">power management framework</a> (PoFx). The PEP can use this handle to identify the device in subsequent communications with PoFx.


### -field DeviceHandle

[out] A PEPHANDLE value that identifies the registration of this device for ACPI services. This handle is created by the PEP. In subsequent ACPI service notifications, PoFx will use this handle to identify the device.


### -field OutputFlags

[out] A set of output flags. No flags are currently defined for this member. Set this member to PEP_ACPI_REGISTER_DEVICE_OUTPUT_FLAG_NONE (0x0).


## -remarks
This structure is used by the <a href="kernel.pep_notify_acpi_register_device">PEP_NOTIFY_ACPI_REGISTER_DEVICE</a> notification. The <b>AcpiDeviceName</b>, <b>InputFlags</b>, and <b>KernelHandle</b> members of the structure contain input values that are supplied by PoFx when this notification is sent to the PEP. The <b>DeviceHandle</b> and <b>OutputFlags</b> members contains output values that the PEP writes to this structure in response to the notification.


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported starting with Windows 10.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Pepfx.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.ansi_string">ANSI_STRING</a>
</dt>
<dt>
<a href="kernel.pep_acpi_prepare_device">PEP_ACPI_PREPARE_DEVICE</a>
</dt>
<dt>
<a href="kernel.pep_dpm_register_device">PEP_DPM_REGISTER_DEVICE</a>
</dt>
<dt>
<a href="kernel.pep_notify_acpi_register_device">PEP_NOTIFY_ACPI_REGISTER_DEVICE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_ACPI_REGISTER_DEVICE structure%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

