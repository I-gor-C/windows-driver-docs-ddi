---
UID: NS.ISCSIOP._MSISCSI_LUNMAPPINGINFORMATION
title: _MSiSCSI_LUNMappingInformation
author: windows-driver-content
description: This MSiSCSI_LUNMappingInformation structure provides the SCSI address information that the operating system assigns to a particular logical unit.
old-location: storage\msiscsi_lunmappinginformation.htm
old-project: storage
ms.assetid: abe4b0fe-3918-4139-9c35-d9399287ce03
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: _MSiSCSI_LUNMappingInformation, *PMSiSCSI_LUNMappingInformation, MSiSCSI_LUNMappingInformation
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iscsiop.h
req.include-header: Iscsiop.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MSiSCSI_LUNMappingInformation
req.alt-loc: iscsiop.h
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
---

# _MSiSCSI_LUNMappingInformation structure



## -description
This MSiSCSI_LUNMappingInformation structure provides the SCSI address information that the operating system assigns to a particular logical unit.



## -syntax

````
typedef struct _MSiSCSI_LUNMappingInformation {
  ULONGLONG UniqueAdapterId;
  ULONGLONG UniqueSessionId;
  ULONG     OSBus;
  ULONG     OSTarget;
  ULONG     OSLUN;
} MSiSCSI_LUNMappingInformation, *PMSiSCSI_LUNMappingInformation;
````


## -struct-fields

### -field UniqueAdapterId

A 64-bit integer that uniquely identifies an HBA initiator and a loaded instance of a storage miniport driver that manages the HBA. The initiator should use the address of the adapter extension or another address that the device driver owns to construct this identifier (ID). The initiator reports this value in the <b>UniqueAdapterId</b> member of the <a href="storage.msiscsi_hbainformation">MSiSCSI_HBAInformation</a> structure.


### -field UniqueSessionId

A session ID that uniquely identifies the session for which the LUN mapping is valid. The <a href="storage.logintotarget">LoginToTarget</a> and <a href="storage.addconnectiontosession">AddConnectionToSession</a> methods both return this value in the <i>UniqueSessionId</i> parameter. Do not confuse this value with the values in the ISID and TSID members.


### -field OSBus

The number that the operating system assigns to the bus that the adapter is attached to.


### -field OSTarget

The device number that the operating system assigns to the target.


### -field OSLUN

The logical unit number (LUN) that the operating system assigns to the logical unit.


## -remarks
You must implement this class.


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Iscsiop.h (include Iscsiop.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.addconnectiontosession">AddConnectionToSession</a>
</dt>
<dt>
<a href="storage.logintotarget">LoginToTarget</a>
</dt>
<dt>
<a href="storage.msiscsi_hbainformation">MSiSCSI_HBAInformation</a>
</dt>
<dt>
<a href="storage.msiscsi_lunmappinginformation_wmi_class">MSiSCSI_LUNMappingInformation WMI Class</a>
</dt>
<dt>
<a href="storage.msiscsi_targetmappings">MSiSCSI_TargetMappings</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20MSiSCSI_LUNMappingInformation structure%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

