---
UID: NC.ntddk.PGET_LOCATION_STRING
title: PGET_LOCATION_STRING
author: windows-driver-content
description: The PnpGetLocationString routine provides the device-specific part of the device's SPDRP_LOCATION_PATHS property.
old-location: kernel\pnpgetlocationstring.htm
old-project: kernel
ms.assetid: 03ebdeed-10f0-4633-a9cd-4db683a8c3a7
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: FILTER_INITIALIZATION_DATA, FILTER_INITIALIZATION_DATA, *PFILTER_INITIALIZATION_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ntddk.h
req.include-header: Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows Server 2003.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PnpGetLocationString
req.alt-loc: Ntddk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= PASSIVE_LEVEL
req.iface: 
---

# PGET_LOCATION_STRING callback



## -description
<p>The <i>PnpGetLocationString</i> routine provides the device-specific part of the device's SPDRP_LOCATION_PATHS property.</p>


## -prototype

````
PGET_LOCATION_STRING PnpGetLocationString;

NTSTATUS PnpGetLocationString(
  _Inout_ PVOID  Context,
  _Out_   PWCHAR *LocationStrings
)
{ ... }
````


## -parameters
<dl>

### -param Context [in, out]

<dd>
<p>A pointer to interface-specific context information.  The caller passes the value that is passed as the <b>Context</b> member of the <a href="..\ntddk\ns-ntddk--pnp-location-interface.md">PNP_LOCATION_INTERFACE</a> structure.</p>
</dd>

### -param LocationStrings [out]

<dd>
<p>A pointer to a sequence of null-terminated Unicode strings, that is terminated by another zero. Each string serves as a location string for the device. Drivers typically return a single string.</p>
</dd>
</dl>

## -returns
<p>The routine returns an NTSTATUS value to indicate the status of the operation.</p>

## -remarks
<p>The <a href="..\ntddk\ns-ntddk--pnp-location-interface.md">PNP_LOCATION_INTERFACE</a> structure supplies a pointer to the <i>PnpGetLocationString</i> routine.</p>

<p>The <i>PnpGetLocationString</i> routine provides the device-specific part of the location string for the device.  The Plug and Play (PnP) manager assembles the location string for a device by querying the driver for the device, for the device's bus, and any parent buses, and concatenating the provided strings together.</p>

<p>The routine must return a string that is unique to the device relative to its bus. The string must be the same for the device across all versions of the operating system. Once you select a string for this purpose, you must not change it.</p>

<p>By convention, the location string takes the form <i>ServiceName(BusSpecificLocation)</i>. For example, PCI devices use PCI(<i>XXYY</i>), where <i>XX</i> is the device number, and <i>YY</i> is the function number.</p>

<p>The <i>PnpGetLocationString</i> routine calls a routine such as <a href="..\wdm\nf-wdm-exallocatepoolwithtag.md">ExAllocatePoolWithTag</a> to allocate the memory for the location string. The caller is responsible for calling the <a href="..\wdm\nf-wdm-exfreepool.md">ExFreePool</a> routine to free the memory pointed to by <i>LocationStrings</i> when the location string is no longer needed.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows Server 2003.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-exallocatepoolwithtag.md">ExAllocatePoolWithTag</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-exfreepool.md">ExFreePool</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--pnp-location-interface.md">PNP_LOCATION_INTERFACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PGET_LOCATION_STRING routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
