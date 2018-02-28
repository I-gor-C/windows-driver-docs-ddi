---
UID: NI:ntddcdvd.IOCTL_AACS_END_SESSION
title: IOCTL_AACS_END_SESSION
author: windows-driver-content
description: Releases the Authentication Grant Identifier (AGID) that was obtained by IOCTL_AACS_START_SESSION.
old-location: storage\ioctl_aacs_end_session.htm
old-project: storage
ms.assetid: 5a86c871-ed6e-4c96-bc12-03b3a900953d
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: IOCTL_AACS_END_SESSION, IOCTL_AACS_END_SESSION control code [Storage Devices], k307_608ddec6-9661-433b-8b82-22ce3b06267d.xml, ntddcdvd/IOCTL_AACS_END_SESSION, storage.ioctl_aacs_end_session
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Ntddcdvd.h
api_name:
-	IOCTL_AACS_END_SESSION
product: Windows
targetos: Windows
req.typenames: DVD_STRUCTURE_FORMAT, *PDVD_STRUCTURE_FORMAT
---

# IOCTL_AACS_END_SESSION IOCTL
Releases the Authentication Grant Identifier (AGID) that was obtained by <a href="..\ntddcdvd\ni-ntddcdvd-ioctl_aacs_start_session.md">IOCTL_AACS_START_SESSION</a>.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> contains a value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff553743">DVD_SESSION_ID</a> that specifies an Authentication Grant Identifier (AGID). The AGID identifies the secure session to release. Caller can release all AGIDs for both Advanced Access Content System (AACS) and Content-Scrambling System (CSS) secure sessions by specifying a value DVD_END_ALL_SESSIONS.

### Input Buffer Length
Size of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff553743">DVD_SESSION_ID</a>.

### Output Buffer
None.

### Output Buffer Length
None.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
The <b>Information</b> field is set to the number of bytes transferred. The <b>Status</b> field is set to STATUS_SUCCESS or possibly STATUS_INSUFFICIENT_RESOURCES.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddcdvd.h (include Ntddcdvd.h) |