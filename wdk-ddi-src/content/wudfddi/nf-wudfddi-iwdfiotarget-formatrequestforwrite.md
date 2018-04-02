---
UID: NF:wudfddi.IWDFIoTarget.FormatRequestForWrite
title: IWDFIoTarget::FormatRequestForWrite method
author: windows-driver-content
description: The FormatRequestForWrite method formats an I/O request object for a write operation.
old-location: wdf\iwdfiotarget_formatrequestforwrite.htm
old-project: wdf
ms.assetid: dd579620-4fe9-4cd0-8e21-f32b07338de1
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: FormatRequestForWrite method, FormatRequestForWrite method, IWDFIoTarget interface, FormatRequestForWrite,IWDFIoTarget.FormatRequestForWrite, IWDFIoTarget, IWDFIoTarget interface, FormatRequestForWrite method, IWDFIoTarget::FormatRequestForWrite, UMDFIoTargetObjectRef_5bd52747-0a43-477e-8240-0481d671a7bb.xml, umdf.iwdfiotarget_formatrequestforwrite, wdf.iwdfiotarget_formatrequestforwrite, wudfddi/IWDFIoTarget::FormatRequestForWrite
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wudfddi.h
req.include-header: Wudfddi.h
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
req.lib: 
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
-	IWDFIoTarget.FormatRequestForWrite
product: Windows
targetos: Windows
req.typenames: POWER_ACTION, *PPOWER_ACTION
req.product: Windows 10 or later.
---


# IWDFIoTarget::FormatRequestForWrite method
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>FormatRequestForWrite</b> method formats an I/O request object for a write operation.

## Syntax

```
HRESULT FormatRequestForWrite(
  IWDFIoRequest     *pRequest,
  IWDFFile          *pFile,
  IWDFMemory        *pInputMemory,
  PWDFMEMORY_OFFSET pInputMemoryOffset,
  PLONGLONG         DeviceOffset
);
```

## Parameters

`pRequest`

A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558985">IWDFIoRequest</a> interface for the request object to format.

`pFile`

A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558912">IWDFFile</a> interface for the file object that is associated with the write request. For the default I/O target, this parameter must be non-<b>NULL</b>.

`pInputMemory`

A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559249">IWDFMemory</a> interface that is used to access the buffer that is used for the write request. This parameter is optional.

`pInputMemoryOffset`

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561398">WDFMEMORY_OFFSET</a> structure that describes the input memory offset that is used for the write request. This parameter is optional.

`DeviceOffset`

A pointer to the device offset that is used for the write request. This parameter is optional.


## Return Value

<b>FormatRequestForWrite</b> returns S_OK if the operation succeeds. Otherwise, this method returns one of the error codes that are defined in Winerror.h.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **End of support** | Unavailable in UMDF 2.0 and later.  |
| **Target Platform** | Desktop |
| **Minimum UMDF version** | 1.5 |
| **Header** | wudfddi.h (include Wudfddi.h) |
| **DLL** | WUDFx.dll |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff558912">IWDFFile</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff558985">IWDFIoRequest</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff559170">IWDFIoTarget</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff559249">IWDFMemory</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561398">WDFMEMORY_OFFSET</a>