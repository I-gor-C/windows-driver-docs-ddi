---
UID: NF:wdm.IoGetDevicePropertyData
title: IoGetDevicePropertyData function
author: windows-driver-content
description: The IoGetDevicePropertyData routine retrieves the current setting for a device property.
old-location: kernel\iogetdevicepropertydata.htm
old-project: kernel
ms.assetid: 3ca026b8-abed-409c-8be4-01553cfadca3
ms.author: windowsdriverdev
ms.date: 3/1/2018
ms.keywords: IoGetDevicePropertyData, IoGetDevicePropertyData routine [Kernel-Mode Driver Architecture], k104_85cb50ca-43cc-401a-8ed1-32ff0c381ed8.xml, kernel.iogetdevicepropertydata, wdm/IoGetDevicePropertyData
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: "<= APC_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	IoGetDevicePropertyData
product: Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# IoGetDevicePropertyData function
The <b>IoGetDevicePropertyData</b> routine retrieves the current setting for a device property.

## Syntax

````
NTSTATUS IoGetDevicePropertyData(
  _In_             PDEVICE_OBJECT Pdo,
  _In_       const DEVPROPKEY     *PropertyKey,
  _In_             LCID           Lcid,
  _Reserved_       ULONG          Flags,
  _In_             ULONG          Size,
  _Out_            PVOID          Data,
  _Out_            PULONG         RequiredSize,
  _Out_            PDEVPROPTYPE   Type
);
````

## Parameters

`Pdo`

A pointer to the physical device object (PDO) for the device that is being queried.

`PropertyKey`

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/dn315031">DEVPROPKEY</a> structure that specifies the device property key.

`Lcid`

A locale identifier. Set this parameter either to a language-specific LCID value or to <b>LOCALE_NEUTRAL</b>. The <b>LOCALE_NEUTRAL</b> LCID specifies that the property is language-neutral (that is, not specific to any language). Do not set this parameter to <b>LOCALE_SYSTEM_DEFAULT</b> or <b>LOCALE_USER_DEFAULT</b>. For more information about language-specific LCID values, see <a href="http://msdn.microsoft.com/en-us/library/cc233968(PROT.10).aspx">LCID Structure</a>.

`Flags`

Reserved for system use. Drivers should set this value to 0.

`Size`

The size, in bytes, of the buffer that <i>Data</i> points to.

`Data`

A pointer to the device property data.

`RequiredSize`

A pointer to a ULONG to receive the size of the property information that is returned at <i>Data</i>. If <b>IoGetDevicePropertyData</b> returns STATUS_BUFFER_TOO_SMALL, the caller can use this value to allocate a buffer of the correct size.

`Type`

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543546">DEVPROPTYPE</a> value. If <b>IoGetDevicePropertyData</b> completes successfully, the routine uses <i>Type</i> to supply the type of data that is returned in the <i>Data</i> buffer.


## Return Value

<b>IoGetDevicePropertyData</b> returns an NTSTATUS value. This routine might return one of the following values:

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>
</td>
<td width="60%">
The operation succeeded. The <i>Data</i> buffer contains the retrieved data. *<i>Type</i> contains the type of the retrieved data.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl>
</td>
<td width="60%">
The <i>Data</i> buffer is too small. *<i>RequiredSize</i> contains the required buffer length.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_OBJECT_NAME_NOT_FOUND</b></dt>
</dl>
</td>
<td width="60%">
The specified device property was not found.

</td>
</tr>
</table>

## Remarks

Kernel-mode drivers use the <b>IoGetDevicePropertyData</b> routine to retrieve device properties that are defined as part of the unified device property model. For more information about device properties, see <a href="https://msdn.microsoft.com/f41040c5-0eac-450d-b532-9165c543cc1a">Device Properties</a>.

Drivers can use the <a href="..\wdm\nf-wdm-iosetdevicepropertydata.md">IoSetDevicePropertyData</a> routine to modify a device property.

Callers of <b>IoGetDevicePropertyData</b> must be running at IRQL &lt;= APC_LEVEL in the context of a system thread.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows Vista.  |
| **Target Platform** | Universal |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | "<= APC_LEVEL" |
| **DDI compliance rules** | PowerIrpDDis, HwStorPortProhibitedDDIs |

## See Also

<a href="..\wdm\nf-wdm-iosetdevicepropertydata.md">IoSetDevicePropertyData</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff543546">DEVPROPTYPE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn315031">DEVPROPKEY</a>