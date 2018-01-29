---
UID : NF:wudfddi.IWDFMemory.CopyFromMemory
title : IWDFMemory::CopyFromMemory method
author : windows-driver-content
description : The CopyFromMemory method safely copies data from the specified source buffer and prevents overruns that the copy operation might otherwise cause.
old-location : wdf\iwdfmemory_copyfrommemory.htm
old-project : wdf
ms.assetid : 29b77215-9c7e-47f2-8c94-0bcd733f54a2
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : IWDFMemory::CopyFromMemory, wudfddi/IWDFMemory::CopyFromMemory, CopyFromMemory method, IWDFMemory interface, UMDFMemoryObjectRef_c5bc961a-62e9-4692-bbd7-6551b268b08b.xml, IWDFMemory, CopyFromMemory, IWDFMemory interface, CopyFromMemory method, CopyFromMemory method, umdf.iwdfmemory_copyfrommemory, wdf.iwdfmemory_copyfrommemory
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : method
req.header : wudfddi.h
req.include-header : Wudfddi.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 1.5
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : Unavailable in UMDF 2.0 and later.
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : wudfddi.h
req.dll : WUDFx.dll
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PPOWER_ACTION, POWER_ACTION"
req.product : Windows 10 or later.
---


# CopyFromMemory method
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>CopyFromMemory</b> method safely copies data from the specified source buffer and prevents overruns that the copy operation might otherwise cause.

## Syntax

````
HRESULT CopyFromMemory(
  [in]           IWDFMemory        *pSource,
  [in, optional] PWDFMEMORY_OFFSET pSourceOffset
);
````

## Parameters

`Source`



`SourceOffset`




## Return Value

<b>CopyFromMemory</b> returns S_OK if the operation succeeds. Otherwise, this method returns one of the error codes that are defined in Winerror.h.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** | 1.5 |
| **Header** | wudfddi.h (include Wudfddi.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<a href="..\wudfddi_types\ns-wudfddi_types-_wdfmemory_offset.md">WDFMEMORY_OFFSET</a>

<a href="..\wudfddi\nn-wudfddi-iwdfmemory.md">IWDFMemory</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFMemory::CopyFromMemory method%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>