---
UID: NF.ntddsd.SdBusOpenInterface
title: SdBusOpenInterface
author: windows-driver-content
description: The SdBusOpenInterface routine obtains an interface from the Secure Digital (SD) bus driver.
old-location: sd\sdbusopeninterface.htm
ms.assetid: a788cd28-81a7-4b8c-b9c5-76dd2b1cd0f3
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: SD
req.header: ntddsd.h
req.include-header: Ntddsd.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SdBusOpenInterface
req.alt-loc: ntddsd.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: < DISPATCH_LEVEL
ms.keywords: SdBusOpenInterface
req.iface: 
---

# SdBusOpenInterface function



## -description
<p>The <b>SdBusOpenInterface</b> routine obtains an interface from the Secure Digital (SD) bus driver.</p>


## -syntax

````
NTSTATUS SdBusOpenInterface(
  _In_  PDEVICE_OBJECT            Pdo,
  _Out_ PSDBUS_INTERFACE_STANDARD InterfaceStandard,
  _In_  USHORT                    Size,
  _In_  USHORT                    Version
);
````


## -parameters
<dl>

### -param <i>Pdo</i> [in]

<dd>
<p>Pointer to the physical device object that the SD bus driver created for the SD device that the device driver manages. The system passes this pointer to the device driver when it calls the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff540521">AddDevice</a> routine.</p>
</dd>

### -param <i>InterfaceStandard</i> [out]

<dd>
<p>Contains, on input, a pointer to a structure of type <a href="https://msdn.microsoft.com/92b8762d-8af3-493c-aa1d-bc245b0cbd83">SDBUS_INTERFACE_STANDARD</a> supplied by the caller. On output, this structure holds pointers to the SD bus interface routines. This structure also contains some context information in its <b>Context</b> member that the caller should pass in every time it calls an interface routine.</p>
</dd>

### -param <i>Size</i> [in]

<dd>
<p>Contains the size, in bytes, of the structure pointed to by <i>InterfaceStandard</i>.</p>
</dd>

### -param <i>Version</i> [in]

<dd>
<p>Must be set to SDBUS_INTERFACE_VERSION.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if the operation succeeds, or the appropriate error code if the operation fails. </p>

## -remarks
<p>An SD card driver should call this routine from its <a href="https://msdn.microsoft.com/library/windows/hardware/ff540521">AddDevice</a> routine.</p>

<p>SD card drivers must call this routine to establish communication with the bus driver. On successful completion of this call, the <b>Context</b> member of the structure pointed to by <i>InterfaceStandard</i> will contain a handle that the driver must pass in when calling methods that belong to the retrieved interface. </p>

<p>An SD card driver should call this routine from its <a href="https://msdn.microsoft.com/library/windows/hardware/ff540521">AddDevice</a> routine.</p>

<p>SD card drivers must call this routine to establish communication with the bus driver. On successful completion of this call, the <b>Context</b> member of the structure pointed to by <i>InterfaceStandard</i> will contain a handle that the driver must pass in when calling methods that belong to the retrieved interface. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddsd.h (include Ntddsd.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt; DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540521">AddDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/92b8762d-8af3-493c-aa1d-bc245b0cbd83">SDBUS_INTERFACE_STANDARD</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [SD\buses]:%20SdBusOpenInterface function%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
