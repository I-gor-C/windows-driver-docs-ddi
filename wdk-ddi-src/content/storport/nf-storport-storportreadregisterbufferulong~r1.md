---
UID: NF.storport.StorPortReadRegisterBufferUlong~r1
title: StorPortReadRegisterBufferUlong macro
author: windows-driver-content
description: The StorPortReadRegisterBufferUlong routine reads a value from a specified register address.
old-location: storage\storportreadregisterbufferulong.htm
old-project: storage
ms.assetid: 069defee-6295-4492-b0bb-135c476c79aa
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: StorPortReadRegisterBufferUlong
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortReadRegisterBufferUlong
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
req.product: Windows 10 or later.
---

# StorPortReadRegisterBufferUlong macro



## -description
The <b>StorPortReadRegisterBufferUlong</b> routine reads a value from a specified register address. 



## -syntax

````
STORPORT_API VOID StorPortReadRegisterBufferUlong(
  _In_ PVOID  HwDeviceExtension,
  _In_ PULONG Register,
  _In_ PULONG Buffer,
  _In_ ULONG  Count
);
````


## -parameters

### -param HwDeviceExtension [in]

Pointer to the hardware device extension.


### -param Register [in]

Pointer to the register where the data is to be read. 


### -param Buffer [in]

Pointer to the buffer that receives the data that is read.


### -param Count [in]

Specifies the number of data items to be read. Each data item has a size of <b>sizeof</b>(ULONG). 


## -remarks
For more information, see <a href="storage.scsiportreadregisterbufferulong">ScsiPortReadRegisterBufferUlong</a>. For a nonbuffered version of this routine, see <a href="storage.storportreadregisterulong">StorPortReadRegisterUlong</a>.


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
Header

</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

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
<a href="storage.scsiportreadregisterbufferulong">ScsiPortReadRegisterBufferUlong</a>
</dt>
<dt>
<a href="storage.storportreadregisterulong">StorPortReadRegisterUlong</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20StorPortReadRegisterBufferUlong routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
