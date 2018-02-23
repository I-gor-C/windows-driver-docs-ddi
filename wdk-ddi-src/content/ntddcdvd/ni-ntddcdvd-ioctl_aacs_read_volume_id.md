---
UID: NI:ntddcdvd.IOCTL_AACS_READ_VOLUME_ID
title: IOCTL_AACS_READ_VOLUME_ID
author: windows-driver-content
description: Reads the Advanced Access Content System (AACS)-specific volume identifier.
old-location: storage\ioctl_aacs_read_volume_id.htm
old-project: storage
ms.assetid: 8772a83a-06e3-48f8-9d41-47332122ec8b
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: storage.ioctl_aacs_read_volume_id, IOCTL_AACS_READ_VOLUME_ID control code [Storage Devices], IOCTL_AACS_READ_VOLUME_ID, ntddcdvd/IOCTL_AACS_READ_VOLUME_ID, k307_ec201772-11c1-4825-8a71-f00f621a1b04.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ntddcdvd.h
req.include-header: Ntddcdvd.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	Ntddcdvd.h
apiname:
-	IOCTL_AACS_READ_VOLUME_ID
product: Windows
targetos: Windows
req.typenames: DVD_STRUCTURE_FORMAT, *PDVD_STRUCTURE_FORMAT
---

# IOCTL_AACS_READ_VOLUME_ID IOCTL
Reads the Advanced Access Content System (AACS)-specific volume identifier.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> contains a value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff553743">DVD_SESSION_ID</a> that specifies an Authentication Grant Identifier (AGID). The AGID identifies the secure session that is associated with the volume.

### Input Buffer Length
Length of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff553743">DVD_SESSION_ID</a>.

### Output Buffer
The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> contains the value of type <a href="..\ntddcdvd\ns-ntddcdvd-_aacs_volume_id.md">AACS_VOLUME_ID</a> that specifies the volume ID.

### Output Buffer Length
Length of a <a href="..\ntddcdvd\ns-ntddcdvd-_aacs_volume_id.md">AACS_VOLUME_ID</a>.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
The <b>Information</b> field is set to the number of bytes transferred. The <b>Status</b> field is set to STATUS_SUCCESS or possibly STATUS_INSUFFICIENT_RESOURCES.

## Remarks
The IOCTL_AACS_READ_VOLUME_ID request corresponds to the part of the AACS authentication protocol that is responsible for transfering the volume identifier. For a complete description of this protocol, see the <i>Advanced Access Content System, Introduction and Common Cryptographic Elements</i> specification that is published by Advanced Access Content System Licensing Administrator (AACS LA). 

The AGID is automatically released after the IOCTL_AACS_READ_VOLUME_ID request completes.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddcdvd.h (include Ntddcdvd.h) |