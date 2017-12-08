---
UID: NF.storport.StorPortWriteRegisterUchar~r1
title: StorPortWriteRegisterUchar
author: windows-driver-content
description: The StorPortWriteRegisterBufferUshort routine transfers a given number of character values from a buffer to the indicated HBA register address.
old-location: storage\storportwriteregisteruchar.htm
old-project: storage
ms.assetid: 731ae55e-8cfb-4b76-b811-dbdabd8dd067
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: StorPortWriteRegisterUchar
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortWriteRegisterUchar
req.alt-loc: Storport.lib,Storport.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Storport.lib
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# StorPortWriteRegisterUchar function



## -description
<p>The <b>StorPortWriteRegisterBufferUshort</b> routine transfers a given number of character values from a buffer to the indicated HBA register address.</p>


## -syntax

````
STORPORT_API VOID StorPortWriteRegisterUchar(
  _In_ PVOID  HwDeviceExtension,
  _In_ PUCHAR Register,
  _In_ UCHAR  Value
);
````


## -parameters
<dl>

### -param HwDeviceExtension [in]

<dd>
<p>A pointer to the hardware device extension. This is a per HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport driver immediately after the miniport driver calls <a href="..\storport\nf-storport-storportinitialize.md">StorPortInitialize</a>. The port driver frees this memory when it removes the device. </p>
</dd>

### -param Register [in]

<dd>
<p>Pointer to the register. The given <i>Register</i> must be in a mapped memory space range returned by <a href="..\storport\nf-storport-storportgetdevicebase.md">StorPortGetDeviceBase</a>. </p>
</dd>

### -param Value [in]

<dd>
<p>Specifies the value to be written to the HBA's register.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Storport.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\srb\nf-srb-scsiportwriteregisterbufferushort.md">ScsiPortWriteRegisterBufferUshort</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20StorPortWriteRegisterUchar routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
