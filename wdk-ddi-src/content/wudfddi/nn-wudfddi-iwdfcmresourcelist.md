---
UID: NN:wudfddi.IWDFCmResourceList
title: IWDFCmResourceList
author: windows-driver-content
description: This interface represents a list of hardware resources for a device.
old-location: wdf\iwdfcmresourcelist.htm
old-project: wdf
ms.assetid: 8C03A1A3-1757-4622-9652-0D84DC0AFE59
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IWDFCmResourceList, IWDFCmResourceList interface, IWDFCmResourceList interface, described, umdf.iwdfcmresourcelist, wdf.iwdfcmresourcelist, wudfddi/IWDFCmResourceList
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
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
-	IWDFCmResourceList
product: Windows
targetos: Windows
req.typenames: POWER_ACTION, *PPOWER_ACTION
req.product: Windows 10 or later.
---

# IWDFCmResourceList interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

This interface represents a list of hardware resources for a device.

## Methods

<p>The <b>IWDFCmResourceList</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDFCmResourceList::GetCount](nf-wudfddi-iwdfcmresourcelist-getcount.md) | The GetCount method returns the number of resource descriptors that are contained in this interface's resource list. |
| [IWDFCmResourceList::GetDescriptor](nf-wudfddi-iwdfcmresourcelist-getdescriptor.md) | The GetDescriptor method returns a pointer to a resource descriptor that is contained in this interface's resource list. |

## Remarks
After a UMDF driver receives a translated resource list in its <a href="https://msdn.microsoft.com/library/windows/hardware/hh439734">OnPrepareHardware</a> callback, it can use <b>IWDFCmResourceList</b> to scan through the list and identify its port and register resources.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **End of support** | Unavailable in UMDF 2.0 and later.  |
| **Target Platform** | Desktop |
| **Minimum UMDF version** | 1.11 |
| **Header** | wudfddi.h |

## See Also

<a href="https://msdn.microsoft.com/2361CEA9-A58C-4019-B4F6-BA1D7DEE3A80">Framework Resource-List Object Methods</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff560200">IWDFObject</a>