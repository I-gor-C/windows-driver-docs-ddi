---
UID: NS.ntddchgr._CHANGER_EXCHANGE_MEDIUM
title: CHANGER_EXCHANGE_MEDIUM
author: windows-driver-content
description: The CHANGER_EXCHANGE_MEDIUM structure is used with the IOCTL_CHANGER_EXCHANGE_MEDIUM request to exchange locations of two pieces of media.
old-location: storage\changer_exchange_medium.htm
old-project: storage
ms.assetid: b0f03d83-61d3-4aa1-ae4e-a8bdc9f13a9f
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: CHANGER_EXCHANGE_MEDIUM, CHANGER_EXCHANGE_MEDIUM, *PCHANGER_EXCHANGE_MEDIUM
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddchgr.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CHANGER_EXCHANGE_MEDIUM
req.alt-loc: ntddchgr.h
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
req.iface: 
---

# CHANGER_EXCHANGE_MEDIUM structure



## -description
<p>The CHANGER_EXCHANGE_MEDIUM structure is used with the <a href="..\ntddchgr\ni-ntddchgr-ioctl-changer-exchange-medium.md">IOCTL_CHANGER_EXCHANGE_MEDIUM</a> request to exchange locations of two pieces of media.</p>


## -syntax

````
typedef struct _CHANGER_EXCHANGE_MEDIUM {
  CHANGER_ELEMENT Transport;
  CHANGER_ELEMENT Source;
  CHANGER_ELEMENT Destination1;
  CHANGER_ELEMENT Destination2;
  BOOLEAN         Flip1;
  BOOLEAN         Flip2;
} CHANGER_EXCHANGE_MEDIUM, *PCHANGER_EXCHANGE_MEDIUM;
````


## -struct-fields
<dl>

### -field Transport

<dd>
<p>Indicates which transport element to use for the exchange operation. This member contains a structure of type <a href="..\ntddchgr\ns-ntddchgr--changer-element.md">CHANGER_ELEMENT</a>. The <b>ElementType</b> member of the CHANGER_ELEMENT structure must be assigned a value of <b>ChangerTransport</b>. </p>
</dd>

### -field Source

<dd>
<p>Indicates the element that contains the piece of media to be moved. </p>
</dd>

### -field Destination1

<dd>
<p>Indicates the destination of the piece of media originally at <b>Source</b>. </p>
</dd>

### -field Destination2

<dd>
<p>Indicates the destination of the piece of media originally at <b>Destination1</b>. </p>
</dd>

### -field Flip1

<dd>
<p>Indicates, when <b>TRUE</b>, that the piece of media moved to <b>Destination1</b> should be flipped. This member is valid only if the <b>Features0</b> member of the <a href="..\ntddchgr\ns-ntddchgr--get-changer-parameters.md">GET_CHANGER_PARAMETERS</a> structure is set to CHANGER_MEDIUM_FLIP. When <b>FALSE</b>, this member indicates that the media does not ready to be flipped. </p>
</dd>

### -field Flip2

<dd>
<p>Indicates, when <b>TRUE</b>, that the medium moved to <b>Destination2</b> should be flipped. This member is valid only if the <b>Features0</b> member of the GET_CHANGER_PARAMETERS structure is set to CHANGER_MEDIUM_FLIP. When <b>FALSE</b>, this member indicates that the media does not ready to be flipped.  </p>
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
<dt>Ntddchgr.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddchgr\ni-ntddchgr-ioctl-changer-exchange-medium.md">IOCTL_CHANGER_EXCHANGE_MEDIUM</a>
</dt>
<dt>
<a href="..\mcd\nf-mcd-changerexchangemedium.md">ChangerExchangeMedium</a>
</dt>
<dt>
<a href="..\ntddchgr\ns-ntddchgr--get-changer-parameters.md">GET_CHANGER_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20CHANGER_EXCHANGE_MEDIUM structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
