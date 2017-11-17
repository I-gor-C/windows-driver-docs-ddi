---
UID: NS.1394._TEXTUAL_LEAF
title: TEXTUAL_LEAF
author: windows-driver-content
description: The TEXTUAL_LEAF structure describes the device description that can be stored in the Configuration ROM of devices that satisfy the PC 98 or PC 99 specifications.
old-location: ieee\textual_leaf.htm
ms.assetid: 883c561c-0d1b-4a6c-946e-8ca567b12c9a
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: IEEE
req.header: 1394.h
req.include-header: 1394.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TEXTUAL_LEAF
req.alt-loc: 1394.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
ms.keywords: TEXTUAL_LEAF, TEXTUAL_LEAF, *PTEXTUAL_LEAF
---

# TEXTUAL_LEAF structure



## -description
<p>The TEXTUAL_LEAF structure describes the device description that can be stored in the Configuration ROM of devices that satisfy the PC 98 or PC 99 specifications.</p>


## -syntax

````
typedef struct _TEXTUAL_LEAF {
  USHORT TL_CRC;
  USHORT TL_Length;
  ULONG  TL_Spec_Id;
  ULONG  TL_Language_Id;
  UCHAR  TL_Data;
} TEXTUAL_LEAF, *PTEXTUAL_LEAF;
````


## -struct-fields
<dl>

### -field <b>TL_CRC</b>

<dd>
<p>Specifies the CRC of the text string.</p>
</dd>

### -field <b>TL_Length</b>

<dd>
<p>Specifies the length of the text string, in bytes.</p>
</dd>

### -field <b>TL_Spec_Id</b>

<dd>
<p>Specifies which specification describes the meaning of the <b>TL_Language_ID</b> member.</p>
</dd>

### -field <b>TL_Language_Id</b>

<dd>
<p>Specifies the language of the <b>TL_Data</b> member.</p>
</dd>

### -field <b>TL_Data</b>

<dd>
<p>Specifies a vendor-specified textual description of the device.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>1394.h (include 1394.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537642">REQUEST_GET_CONFIGURATION_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [IEEE\buses]:%20TEXTUAL_LEAF structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
