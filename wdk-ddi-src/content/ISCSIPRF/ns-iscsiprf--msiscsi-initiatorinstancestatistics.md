---
UID: NS.iscsiprf._MSiSCSI_InitiatorInstanceStatistics
title: MSiSCSI_InitiatorInstanceStatistics
author: windows-driver-content
description: The MSiSCSI_InitiatorInstanceStatistics structure is used by iSCSI initiators to report initiator statistics.
old-location: storage\msiscsi_initiatorinstancestatistics.htm
ms.assetid: b07b8186-970a-428f-955f-4e7e6ab20bfc
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: iscsiprf.h
req.include-header: Iscsiprf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MSiSCSI_InitiatorInstanceStatistics
req.alt-loc: iscsiprf.h
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
ms.keywords: MSiSCSI_InitiatorInstanceStatistics, MSiSCSI_InitiatorInstanceStatistics, *PMSiSCSI_InitiatorInstanceStatistics
req.iface: 
---

# MSiSCSI_InitiatorInstanceStatistics structure



## -description
<p>The MSiSCSI_InitiatorInstanceStatistics structure is used by iSCSI initiators to report initiator statistics.</p>


## -syntax

````
typedef struct _MSiSCSI_InitiatorInstanceStatistics {
  ULONGLONG UniqueAdapterId;
  ULONG     SessionDigestErrorCount;
  ULONG     SessionConnectionTimeoutErrorCount;
  ULONG     SessionFormatErrorCount;
  ULONG     SessionFailureCount;
} MSiSCSI_InitiatorInstanceStatistics, *PMSiSCSI_InitiatorInstanceStatistics;
````


## -struct-fields
<dl>

### -field <b>UniqueAdapterId</b>

<dd>
<p>A 64-bit integer that uniquely identifies an HBA initiator and a loaded instance of a storage miniport driver that manages the HBA. The initiator should use the address of the adapter extension or another address that the device driver owns to construct this identifier (ID). The initiator reports this value in the <b>UniqueAdapterId</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563012">MSiSCSI_HBAInformation</a> structure. For more information about the class that generates MSiSCSI_HBAInformation, see  <a href="https://msdn.microsoft.com/library/windows/hardware/ff563017">MSiSCSI_HBAInformation WMI Class</a>.</p>
</dd>

### -field <b>SessionDigestErrorCount</b>

<dd>
<p>The number of session digest errors.</p>
</dd>

### -field <b>SessionConnectionTimeoutErrorCount</b>

<dd>
<p>The number of session connection time-out errors.</p>
</dd>

### -field <b>SessionFormatErrorCount</b>

<dd>
<p>The number of session format errors.</p>
</dd>

### -field <b>SessionFailureCount</b>

<dd>
<p>The number of failed sessions that belong to the initiator instance that <b>UniqueAdapterId</b> specifies.</p>
</dd>
</dl>

## -remarks
<p>It is optional that you implement this class.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Iscsiprf.h (include Iscsiprf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563012">MSiSCSI_HBAInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563017">MSiSCSI_HBAInformation WMI Class</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563038">MSiSCSI_InitiatorInstanceStatistics WMI Class</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20MSiSCSI_InitiatorInstanceStatistics structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
