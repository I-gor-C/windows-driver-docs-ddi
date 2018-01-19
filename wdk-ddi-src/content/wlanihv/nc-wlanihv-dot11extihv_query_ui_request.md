---
UID : NC:wlanihv.DOT11EXTIHV_QUERY_UI_REQUEST
title : DOT11EXTIHV_QUERY_UI_REQUEST
author : windows-driver-content
description : Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location : netvista\dot11extihvqueryuirequest.htm
old-project : netvista
ms.assetid : 37c01180-0742-4764-88c3-9ceb807a0086
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _DRIVER_INFO_8W, *LPDRIVER_INFO_8W, *PDRIVER_INFO_8W, DRIVER_INFO_8W, DRIVER_INFO_8
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : wlanihv.h
req.include-header : Wlanihv.h
req.target-type : Desktop
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating   systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : Dot11ExtIhvQueryUIRequest
req.alt-loc : wlanihv.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*LPDRIVER_INFO_8W, *PDRIVER_INFO_8W, DRIVER_INFO_8W"
req.product : Windows 10 or later.
---


# DOT11EXTIHV_QUERY_UI_REQUEST callback function


## Syntax

```
DOT11EXTIHV_QUERY_UI_REQUEST Dot11extihvQueryUiRequest;

DWORD Dot11extihvQueryUiRequest(
  HANDLE hIhvExtAdapter,
  DOT11EXT_IHV_CONNECTION_PHASE connectionPhase,
  PDOT11EXT_IHV_UI_REQUEST *ppIhvUIRequest
)
{...}
```

## Parameters

`hIhvExtAdapter`

The handle used by the IHV Extensions DLL to reference the wireless LAN (WLAN) adapter. This
     handle value was specified through a previous call to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv_init_adapter.md">Dot11ExtIhvInitAdapter</a> IHV
     Handler function.

`connectionPhase`

The current connection phase. The data type for this member is the 
     <b>DOT11EXT_IHV_CONNECTION_PHASE</b> enumeration:

`*ppIhvUIRequest`




## Return Value

If the call succeeds, the function returns ERROR_SUCCESS. Otherwise, it returns an error code
     defined in 
     Winerror.h.

## Remarks

When 
    <i>Dot11ExtIhvQueryUIRequest</i> is called, the IHV Extensions DLL must allocate and return a buffer
    formatted as a 
    <a href="..\wlanihv\ns-wlanihv-_dot11ext_ihv_ui_request.md">DOT11EXT_IHV_UI_REQUEST</a> structure.
    In this situation, the DLL must follow these guidelines:

The IHV Extensions DLL must call 
      <a href="..\wlanihv\nc-wlanihv-dot11ext_allocate_buffer.md">Dot11ExtAllocateBuffer</a> to
      allocate the buffer. After the DLL returns from 
      <i>Dot11ExtIhvQueryUIRequest</i>, the operating system is responsible for calling 
      <a href="..\wlanihv\nc-wlanihv-dot11ext_free_buffer.md">Dot11ExtFreeBuffer</a> to free the
      buffer.

The IHV Extensions DLL formats the 
      <a href="..\wlanihv\ns-wlanihv-_dot11ext_ihv_ui_request.md">DOT11EXT_IHV_UI_REQUEST</a> structure
      for a UI request appropriate for the change in connection status.

For example, if 
      <i>connectionPhase</i> is set to 
      <b>connection_phase_initial_connection</b>, the IHV Extensions DLL could set the members of the
      DOT11EXT_IHV_UI_REQUEST structure to reference a user interface page that notifies the user of the
      start of the connection operation.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wlanihv.h (include Wlanihv.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext_allocate_buffer.md">Dot11ExtAllocateBuffer</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext_free_buffer.md">Dot11ExtFreeBuffer</a>
</dt>
<dt>
<a href="..\wlanihv\ns-wlanihv-_dot11ext_ihv_ui_request.md">DOT11EXT_IHV_UI_REQUEST</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv_init_adapter.md">Dot11ExtIhvInitAdapter</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11EXTIHV_QUERY_UI_REQUEST callback function%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>