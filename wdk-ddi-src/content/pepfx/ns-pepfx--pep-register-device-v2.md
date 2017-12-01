---
UID: NS.pepfx._PEP_REGISTER_DEVICE_V2
title: PEP_REGISTER_DEVICE_V2
author: windows-driver-content
description: The PEP_REGISTER_DEVICE_V2 structure describes a device whose driver stack has just registered with the Windows power management framework (PoFx).
old-location: kernel\pep_register_device_v2.htm
old-project: kernel
ms.assetid: A1363B34-CC5C-482E-8E8D-62D7263545E3
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_REGISTER_DEVICE_V2, PEP_REGISTER_DEVICE_V2, *PPEP_REGISTER_DEVICE_V2
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
req.alt-api: PEP_REGISTER_DEVICE_V2
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
req.iface: 
---

# PEP_REGISTER_DEVICE_V2 structure



## -description
<p>The <b>PEP_REGISTER_DEVICE_V2</b> structure describes a device whose driver stack has just registered with the Windows <a href="https://msdn.microsoft.com/9F2D8ACD-44D5-46E0-9FC7-1B38B99450FF">power management framework</a> (PoFx).</p>


## -syntax

````
typedef struct _PEP_REGISTER_DEVICE_V2 {
  PCUNICODE_STRING           DeviceId;
  POHANDLE                   KernelHandle;
  PPEP_DEVICE_REGISTER_V2    Register;
  PEPHANDLE                  DeviceHandle;
  PEP_DEVICE_ACCEPTANCE_TYPE DeviceAccepted;
} PEP_REGISTER_DEVICE_V2, *PPEP_REGISTER_DEVICE_V2;
````


## -struct-fields
<dl>

### -field <b>DeviceId</b>

<dd>
<p>[in] A string that uniquely identifies the device. This member is a pointer to a <a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a> structure that contains a <a href="devinst.device_identification_strings">device identification string</a>.</p>
</dd>

### -field <b>KernelHandle</b>

<dd>
<p>[in] A POHANDLE value that represents the registration of the device with PoFx. The platform extension plug-in (PEP) previously received this handle from PoFx during the <a href="kernel.pep_dpm_register_device">PEP_DPM_REGISTER_DEVICE</a> notification that informed the PEP that the device's driver stack registered the device with PoFx.</p>
</dd>

### -field <b>Register</b>

<dd>
<p>[in] A pointer to a <a href="..\pepfx\ns-pepfx--pep-device-register-v2.md">PEP_DEVICE_REGISTER_V2</a> structure that describes the power management attributes of all the components in the device. For more information, see Remarks.</p>
</dd>

### -field <b>DeviceHandle</b>

<dd>
<p>[out] A PEPHANDLE value that the PEP creates to identify this device.  PoFx will use this handle to identify the device in future <a href="kernel.device_power_management__dpm__notifications">device power management (DPM) notifications</a>.</p>
</dd>

### -field <b>DeviceAccepted</b>

<dd>
<p>[out] A <a href="..\pepfx\ne-pepfx--pep-device-acceptance-type.md">PEP_DEVICE_ACCEPTANCE_TYPE</a> enumeration value that indicates whether the PEP claims ownership of the device. The PEP that claims ownership is responsible for handling DPM notifications for the device.</p>
</dd>
</dl>

## -remarks
<p>This structure is used by the <a href="kernel.pep_dpm_register_device">PEP_DPM_REGISTER_DEVICE</a> notification. The first three members of this structure contain input values supplied by PoFx. The last two members contain output values that the PEP writes to the structure in response to this notification.</p>

<p>The <b>Register</b> member contains a pointer to an input buffer allocated by PoFx. PoFx writes the <a href="..\pepfx\ns-pepfx--pep-device-register-v2.md">PEP_DEVICE_REGISTER_V2</a> structure and associated data to this structure before sending the <a href="kernel.pep_dpm_register_device">PEP_DPM_REGISTER_DEVICE</a> notification to the PEP. The contents of this buffer remain valid only until the PEP finishes handling the notification and returns from the <a href="kernel.acceptdevicenotification">AcceptDeviceNotification</a> callback.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with Windows 10.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
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
<a href="kernel.acceptdevicenotification">AcceptDeviceNotification</a>
</dt>
<dt>
<a href="kernel.pep_dpm_register_device">PEP_DPM_REGISTER_DEVICE</a>
</dt>
<dt>
<a href="..\pepfx\ns-pepfx--pep-device-register-v2.md">PEP_DEVICE_REGISTER_V2</a>
</dt>
<dt>
<a href="..\pepfx\ne-pepfx--pep-device-acceptance-type.md">PEP_DEVICE_ACCEPTANCE_TYPE</a>
</dt>
<dt>
<a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_REGISTER_DEVICE_V2 structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
