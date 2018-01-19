---
UID : NN:portcls.IResourceList
title : IResourceList
author : windows-driver-content
description : The IResourceList interface provides an abstraction of a configuration resource list, which is a list of the system hardware resources that the Plug and Play manager assigns to a device at startup time.
old-location : audio\iresourcelist.htm
old-project : audio
ms.assetid : e99ed3bc-368c-433f-ad40-98deda668c51
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : PcUnregisterIoTimeout
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : portcls.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IResourceList
req.alt-loc : portcls.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Portcls.lib
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : PC_EXIT_LATENCY, *PPC_EXIT_LATENCY
---

# IResourceList interface

The <code>IResourceList</code> interface provides an abstraction of a configuration resource list, which is a list of the system hardware resources that the Plug and Play manager assigns to a device at startup time. The resources in the list can include interrupt vectors, DMA channels, I/O port addresses, and blocks of bus-relative memory addresses. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563856">Starting a Device in a Function Driver</a>.

The PortCls system driver implements the <code>IResourceList</code> interface and exposes it to adapter drivers. When PortCls calls an adapter driver's device-startup routine (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563849">Starting a Device</a>), it passes an <code>IResourceList</code> object as one of the call parameters. 

The header file portcls.h defines set of macros to simplify the handling of resource list objects. For each type of resource, the following four macros are defined:

## Methods

<p>The <b>IResourceList</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [portcls.IResourceList.AddEntry](nf-portcls-iresourcelist-addentry.md) | The AddEntry method adds an entry to a resource list. |
| [portcls.IResourceList.AddEntryFromParent](nf-portcls-iresourcelist-addentryfromparent.md) | The AddEntryFromParent method adds to a resource list an entry found in the resource list's parent list. |
| [portcls.IResourceList.FindTranslatedEntry](nf-portcls-iresourcelist-findtranslatedentry.md) | The FindTranslatedEntry method returns a pointer to a translated entry of the specified type, or NULL if no such entry is found. |
| [portcls.IResourceList.FindUntranslatedEntry](nf-portcls-iresourcelist-finduntranslatedentry.md) | The FindUntranslatedEntry method returns a pointer to an untranslated entry of the specified type, or NULL if no such pointer is found. |
| [portcls.IResourceList.NumberOfEntries](nf-portcls-iresourcelist-numberofentries.md) | The NumberOfEntries method returns the number of resource items in the resource list. |
| [portcls.IResourceList.NumberOfEntriesOfType](nf-portcls-iresourcelist-numberofentriesoftype.md) | The NumberOfEntriesOfType method returns the number of resource items of a given type in the resource list. For each resource type, a macro is defined to call this method as previously described. |
| [portcls.IResourceList.TranslatedList](nf-portcls-iresourcelist-translatedlist.md) | The TranslatedList method returns the list of translated resources. |
| [portcls.IResourceList.UntranslatedList](nf-portcls-iresourcelist-untranslatedlist.md) | The UntranslatedList method returns the list of untranslated resources. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | portcls.h |
| **DLL** |  |