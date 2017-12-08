---
UID: NS.NDISWWAN._NDIS_WWAN_SMS_READ
title: _NDIS_WWAN_SMS_READ
author: windows-driver-content
description: The NDIS_WWAN_SMS_READ structure represents an SMS message to read.
old-location: netvista\ndis_wwan_sms_read.htm
old-project: netvista
ms.assetid: 2c15c16f-773b-415d-80a1-fd0b3bcf6fbf
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _NDIS_WWAN_SMS_READ, NDIS_WWAN_SMS_READ, *PNDIS_WWAN_SMS_READ
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndiswwan.h
req.include-header: Ndiswwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_WWAN_SMS_READ
req.alt-loc: ndiswwan.h
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

# _NDIS_WWAN_SMS_READ structure



## -description
The NDIS_WWAN_SMS_READ structure represents an SMS message to read.


## -syntax

````
typedef struct _NDIS_WWAN_SMS_READ {
  NDIS_OBJECT_HEADER Header;
  WWAN_SMS_READ      SmsRead;
} NDIS_WWAN_SMS_READ, *PNDIS_WWAN_SMS_READ;
````


## -struct-fields

### -field Header

The header with type, revision, and size information about the NDIS_WWAN_SMS_READ structure. The
     MB Service sets the header with the values that are shown in the following table when it sends the data
     structure to the miniport driver for 
     <i>set</i> operations. Miniport drivers must set the header with the same values when they send the data
     structure to the MB service.
     
<table>
<tr>
<th>Header submember</th>
<th>Value</th>
</tr>
<tr>
<td>
Type
</td>
<td>
NDIS_OBJECT_TYPE_DEFAULT
</td>
</tr>
<tr>
<td>
Revision
</td>
<td>
NDIS_WWAN_SMS_READ_REVISION_1
</td>
</tr>
<tr>
<td>
Size
</td>
<td>
sizeof(NDIS_WWAN_SMS_READ)
</td>
</tr>
</table>
 
For more information about these members, see 
     <a href="netvista.ndis_object_header">NDIS_OBJECT_HEADER</a>.

### -field SmsRead

A formatted 
     <a href="netvista.wwan_sms_read">WWAN_SMS_READ</a> object that represents the
     format and filter of SMS messages to read.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available in Windows 7 and later versions of Windows.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ndiswwan.h (include Ndiswwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.ndis_object_header">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="netvista.wwan_sms_read">WWAN_SMS_READ</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_WWAN_SMS_READ structure%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
