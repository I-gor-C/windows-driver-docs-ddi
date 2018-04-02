---
UID: NF:ntifs.IoPageRead
title: IoPageRead function
author: windows-driver-content
description: Reserved for system use.
old-location: ifsk\iopageread.htm
old-project: ifsk
ms.assetid: d1cbd6ee-6625-47bd-bf3e-356b28ff17a5
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: IoPageRead, IoPageRead function [Installable File System Drivers], ifsk.iopageread, ioref_2c5776f2-eef8-49e5-ade1-3ed0edcd6102.xml, ntifs/IoPageRead
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
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
-	ntifs.h
api_name:
-	IoPageRead
product: Windows
targetos: Windows
req.typenames: TOKEN_TYPE
---


# IoPageRead function
The <b>IoPageRead</b> routine is reserved for system use. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff539038">CcCopyRead</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff539159">CcMdlRead</a>.

## Syntax

```
NTKERNELAPI NTSTATUS IoPageRead(
  PFILE_OBJECT     FileObject,
  PMDL             MemoryDescriptorList,
  PLARGE_INTEGER   StartingOffset,
  PKEVENT          Event,
  PIO_STATUS_BLOCK IoStatusBlock
);
```

## Parameters

`FileObject`

TBD

`MemoryDescriptorList`

TBD

`StartingOffset`

TBD

`Event`

TBD

`IoStatusBlock`

TBD


## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | ntifs.h (include Ntifs.h) |