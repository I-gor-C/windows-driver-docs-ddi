---
UID: NS.storport.PPRO_PARAMETER_LIST
title: PPRO_PARAMETER_LIST
author: windows-driver-content
description: The PRO_PARAMETER_LIST structure is sent in a Persistent Reserve Out command to a device server.
old-location: storage\pro_parameter_list.htm
old-project: storage
ms.assetid: 96c128e1-c38a-412f-adeb-cde820e1af4e
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PPRO_PARAMETER_LIST, PRO_PARAMETER_LIST, *PPRO_PARAMETER_LIST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: storport.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PRO_PARAMETER_LIST
req.alt-loc: storport.h
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
req.product: Windows 10 or later.
---

# PPRO_PARAMETER_LIST structure



## -description
<p>The PRO_PARAMETER_LIST structure is sent in a Persistent Reserve Out command to a device server.</p>


## -syntax

````
typedef struct {
  UCHAR ReservationKey[8];
  UCHAR ServiceActionReservationKey[8];
  UCHAR ScopeSpecificAddress[4];
  UCHAR ActivatePersistThroughPowerLoss  :1;
  UCHAR Reserved1  :7;
  UCHAR Reserved2;
  UCHAR Obsolete[2];
} PRO_PARAMETER_LIST, *PPRO_PARAMETER_LIST;
````


## -struct-fields
<dl>

### -field <b>ReservationKey</b>

<dd>
<p>The ReservationKey field contains an 8-byte value that is provided by the application client to the device server. This value identifies the initiator that is the source of the Persistent Reserve Out command.</p>
</dd>

### -field <b>ServiceActionReservationKey</b>

<dd>
<p>The ServiceActionReservationKey field contains information that is needed for the following four service actions:</p>
<ul>
<li>
<p>REGISTER</p>
</li>
<li>
<p>REGISTER AND IGNORE EXISTING KEY</p>
</li>
<li>
<p>PREEMPT</p>
</li>
<li>
<p>PREEMPT AND ABORT</p>
</li>
</ul>
</dd>

### -field <b>ScopeSpecificAddress</b>

<dd>
<p>The ScopeSpecificAddress field contains the element address that has zeros placed in the most significant bits to fit the field. This is true if the scope of a reservation is set to ELEMENT_SCOPE. Otherwise, this field is set to all zeros.</p>
</dd>

### -field <b>ActivatePersistThroughPowerLoss</b>

<dd>
<p>The ActivatePersistThroughPowerLoss (APTPL) bit is valid only for the following service actions:</p>
<ul>
<li>
<p>REGISTER</p>
</li>
<li>
<p>REGISTER AND IGNORE EXISTING KEY</p>
</li>
</ul>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved. Must be zero.</p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>Reserved. Must be zero.</p>
</dd>

### -field <b>Obsolete</b>

<dd>
<p>Reserved. Must be zero.</p>
</dd>
</dl>

## -remarks
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff560586">IOCTL_STORAGE_PERSISTENT_RESERVE_OUT</a> request is used to control information about persistent reservations and reservation keys that are active within a device server.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Ntddstor.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560586">IOCTL_STORAGE_PERSISTENT_RESERVE_OUT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20PRO_PARAMETER_LIST structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
