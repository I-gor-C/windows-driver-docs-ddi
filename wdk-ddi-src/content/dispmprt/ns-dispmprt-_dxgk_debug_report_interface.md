---
UID: NS.DISPMPRT._DXGK_DEBUG_REPORT_INTERFACE
title: _DXGK_DEBUG_REPORT_INTERFACE
author: windows-driver-content
description: The DXGK_DEBUG_REPORT_INTERFACE structure contains pointers to functions in the Debug Report interface, which is implemented by the display port driver.
old-location: display\dxgk_debug_report_interface.htm
old-project: display
ms.assetid: fb1bd1dd-feab-4aa4-8b4f-932f0d5ec4ab
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _DXGK_DEBUG_REPORT_INTERFACE, *PDXGK_DEBUG_REPORT_INTERFACE, DXGK_DEBUG_REPORT_INTERFACE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_DEBUG_REPORT_INTERFACE
req.alt-loc: dispmprt.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
---

# _DXGK_DEBUG_REPORT_INTERFACE structure



## -description
The DXGK_DEBUG_REPORT_INTERFACE structure contains pointers to functions in the <a href="display.debug_report_interface">Debug Report interface</a>, which is implemented by the display port driver.


## -syntax

````
typedef struct _DXGK_DEBUG_REPORT_INTERFACE {
  USHORT                   Size;
  USHORT                   Version;
  PVOID                    Context;
  PINTERFACE_REFERENCE     InterfaceReference;
  PINTERFACE_DEREFERENCE   InterfaceDereference;
  DXGK_DEBUG_REPORT_HANDLE (*DbgReportCreate)(
      _In_ HANDLE DeviceHandle, 
      _In_ ULONG ulCode, 
      _In_ ULONG_PTR ulpArg1, 
      _In_ ULONG_PTR ulpArg2, 
      _In_ ULONG_PTR ulpArg3, 
      _In_ ULONG_PTR ulpArg4);
  BOOLEAN                  (*DbgReportSecondaryData)(
      _Inout_ DXGK_DEBUG_REPORT_HANDLE hReport, 
      _In_ PVOID pvData, 
      _In_ ULONG ulDataSize);
  VOID                     (*DbgReportComplete)(_Inout_ DXGK_DEBUG_REPORT_HANDLE hReport);
} DXGK_DEBUG_REPORT_INTERFACE, *PDXGK_DEBUG_REPORT_INTERFACE;
````


## -struct-fields

### -field Size

The size, in bytes, of this structure.

### -field Version

The version number of the Debug Report interface. Version number constants are defined in <i>Dispmprt.h</i> (for example, DXGK_DEBUG_REPORT_INTERFACE_VERSION_1).

### -field Context

A pointer to a context that is provided by the display port driver.

### -field InterfaceReference

A pointer to an interface reference function that is implemented by the display port driver.

### -field InterfaceDereference

A pointer to an interface dereference function that is implemented by the display port driver.

### -field DbgReportCreate

A pointer to the display port driver's <a href="display.dbgreportcreate2">DbgReportCreate</a> function.

### -field DbgReportSecondaryData

A pointer to the display port driver's <a href="display.dbgreportsecondarydata2">DbgReportSecondaryData</a> function.

### -field DbgReportComplete

A pointer to the display port driver's <a href="display.dbgreportcomplete">DbgReportComplete</a> function. 

## -remarks
The display miniport driver supplies the <b>Size</b> and <b>Version</b> members of this structure, and then calls <a href="..\dispmprt\nc-dispmprt-dxgkcb_query_services.md">DxgkCbQueryServices</a>, which fills in the remaining members of this structure.

## -requirements
<table>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available in Windows Vista and later versions of the Windows operating systems.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Dispmprt.h (include Dispmprt.h)</dt>
</dl>
</td>
</tr>
</table>