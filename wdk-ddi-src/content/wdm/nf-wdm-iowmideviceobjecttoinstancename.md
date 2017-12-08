---
UID: NF.wdm.IoWMIDeviceObjectToInstanceName
title: IoWMIDeviceObjectToInstanceName function
author: windows-driver-content
description: The IoWMIDeviceObjectToInstanceName routine determines the instance name for the WMI class instance implemented by the driver that is specified by a device object.
old-location: kernel\iowmideviceobjecttoinstancename.htm
old-project: kernel
ms.assetid: 18692c0d-8b74-495d-b66a-2873837ff797
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: IoWMIDeviceObjectToInstanceName
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows XP and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoWMIDeviceObjectToInstanceName
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= APC_LEVEL
req.product: Windows 10 or later.
---

# IoWMIDeviceObjectToInstanceName function



## -description
The <b>IoWMIDeviceObjectToInstanceName</b> routine determines the instance name for the WMI class instance implemented by the driver that is specified by a device object.


## -syntax

````
NTSTATUS IoWMIDeviceObjectToInstanceName(
  _In_  PVOID           DataBlockObject,
  _In_  PDEVICE_OBJECT  DeviceObject,
  _Out_ PUNICODE_STRING InstanceName
);
````


## -parameters

### -param DataBlockObject [in]

Pointer to a WMI data block object. The caller opens the data block object for the WMI class with <a href="kernel.iowmiopenblock">IoWMIOpenBlock</a>.

### -param DeviceObject [in]

Specifies a device object. The routine returns the instance name for the driver corresponding to the device object.

### -param InstanceName [out]

Pointer to the <a href="kernel.unicode_string">UNICODE_STRING</a> structure that the routine uses to return the instance name. The caller frees the returned buffer within <b>UNICODE_STRING</b>.

## -returns
The routine returns an NTSTATUS code. Possible return values include:
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The operation succeeded. The routine stores the instance name in the <b>UNICODE_STRING</b> specified by the <i>InstanceName</i> parameter.
<dl>
<dt><b>STATUS_WMI_INSTANCE_NOT_FOUND</b></dt>
</dl>The driver does not implement any instances of the WMI class specified by <i>DataBlockObject</i>.

 

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available in Windows XP and later versions of the Windows operating system.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
&lt;= APC_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.device_object">DEVICE_OBJECT</a>
</dt>
<dt>
<a href="kernel.iowmiopenblock">IoWMIOpenBlock</a>
</dt>
<dt>
<a href="kernel.iowmihandletoinstancename">IoWMIHandleToInstanceName</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoWMIDeviceObjectToInstanceName routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
