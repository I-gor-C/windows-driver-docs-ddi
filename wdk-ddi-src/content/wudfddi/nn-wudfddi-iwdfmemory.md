---
UID: NN:wudfddi.IWDFMemory
title: IWDFMemory
author: windows-driver-content
description: The IWDFMemory interface exposes the framework memory object that provides access to a memory block.
old-location: wdf\iwdfmemory.htm
old-project: wdf
ms.assetid: 8746eb43-7a6e-4e1d-b8fb-c8b7891295d6
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: IWDFMemory, IWDFMemory interface, IWDFMemory interface, described, UMDFMemoryObjectRef_14266bd8-214b-4244-a96b-9bea5cfa9d84.xml, umdf.iwdfmemory, wdf.iwdfmemory, wudfddi/IWDFMemory
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: wudfddi.h
req.dll: WUDFx.dll
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	WUDFx.dll
api_name:
-	IWDFMemory
product: Windows
targetos: Windows
req.typenames: POWER_ACTION, *PPOWER_ACTION
req.product: Windows 10 or later.
---

# IWDFMemory interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IWDFMemory</b> interface exposes the framework memory object that provides access to a memory block.

## Methods

<p>The <b>IWDFMemory</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDFMemory::CopyFromBuffer](nf-wudfddi-iwdfmemory-copyfrombuffer.md) | The CopyFromBuffer method safely copies data from the specified source buffer to a memory object. |
| [IWDFMemory::CopyFromMemory](nf-wudfddi-iwdfmemory-copyfrommemory.md) | The CopyFromMemory method safely copies data from the specified source buffer and prevents overruns that the copy operation might otherwise cause. |
| [IWDFMemory::CopyToBuffer](nf-wudfddi-iwdfmemory-copytobuffer.md) | The CopyToBuffer method safely copies data from a memory object to the specified target buffer. |
| [IWDFMemory::GetDataBuffer](nf-wudfddi-iwdfmemory-getdatabuffer.md) | The GetDataBuffer method retrieves the data buffer that is associated with a memory object. |
| [IWDFMemory::GetSize](nf-wudfddi-iwdfmemory-getsize.md) | The GetSize method retrieves the size of the data buffer that is associated with a memory object. |
| [IWDFMemory::SetBuffer](nf-wudfddi-iwdfmemory-setbuffer.md) | The SetBuffer method assigns a specified buffer to a memory object that a driver created by calling IWDFDriver::CreatePreallocatedWdfMemory. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **End of support** | Unavailable in UMDF 2.0 and later.  |
| **Target Platform** | Desktop |
| **Minimum UMDF version** | 1.5 |
| **Header** | wudfddi.h |