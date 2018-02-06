---
UID: NS:d3dukmdt._D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS
title: "_D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS"
author: windows-driver-content
description: Identifies attributes of a synchronization object.
old-location: display\d3dddi_synchronizationobject_flags.htm
old-project: display
ms.assetid: 57e5ea18-ccdd-40a7-9ff5-4d6b94908e7c
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: "_D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS, D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS, d3dukmdt/D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS, D3D_other_Structs_3d266c5b-53c9-47d1-abe9-f492d05660a4.xml, D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS structure [Display Devices], display.d3dddi_synchronizationobject_flags"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dumddi.h, D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS is supported beginning with the Windows 7 operating system.
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
-	d3dukmdt.h
apiname:
-	D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS
product: Windows
targetos: Windows
req.typenames: D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS
---

# _D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS structure
Identifies attributes of a synchronization object.

## Syntax
````
typedef struct _D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS {
  union {
    struct {
      UINT Shared  :1;
      UINT NtSecuritySharing  :1;
#if ((DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM1_3) || \
     (D3D_UMD_INTERFACE_VERSION >= D3D_UMD_INTERFACE_VERSION_WDDM1_3))
      UINT CrossAdapter  :1;
#if ((DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_0) || \
     (D3D_UMD_INTERFACE_VERSION >= D3D_UMD_INTERFACE_VERSION_WDDM2_0))
      UINT TopOfPipeline  :1;
      UINT NoSignal  :1;
      UINT NoWait  :1;
      UINT NoSignalMaxValueOnTdr  :1;
      UINT Reserved  :24;
#else 
      UINT Reserved  :28;
#endif 
#else 
      UINT Reserved  :29;
#endif 
      UINT D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS_RESERVED0  :1;
    };
    UINT Value;
  };
} D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS;
````

## Members


## Remarks
Objects to be shared by using the <a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtshareobjects.md">D3DKMTShareObjects</a> function must first be created with the <b>NtSecuritySharing</b> flag value set. This flag value is available in the <a href="..\d3dkmthk\ns-d3dkmthk-_d3dkmt_createallocationflags.md">D3DKMT_CREATEALLOCATIONFLAGS</a>, <a href="..\d3dkmthk\ns-d3dkmthk-_d3dkmt_createkeyedmutex2_flags.md">D3DKMT_CREATEKEYEDMUTEX2_FLAGS</a>, and <b>D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS</b> structures.

Drivers should follow these guidelines on <b>D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS</b> flags:
<ul>
<li>If the synchronization object is not shared, set both  <b>Shared</b> and <b>NtSecuritySharing</b> to 0.</li>
<li>If the synchronization object is shared with a <b>D3DKMT_HANDLE</b> data type, set <b>Shared</b> = 1 and <b>NtSecuritySharing</b> = 0.</li>
<li>If the synchronization object is shared with an NT handle to the process (and without a global <b>D3DKMT_HANDLE</b> kernel-mode handle to the resource), set <b>Shared</b> = 1 and <b>NtSecuritySharing</b> = 1.</li>
</ul>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS is supported beginning with the Windows 7 operating system. D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS is supported beginning with the Windows 7 operating system. |
| **Header** | d3dukmdt.h (include D3dumddi.h, D3dkmddi.h) |

## See Also

<a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtshareobjects.md">D3DKMTShareObjects</a>

<a href="..\d3dukmdt\ns-d3dukmdt-_d3dddi_synchronizationobjectinfo2.md">D3DDDI_SYNCHRONIZATIONOBJECTINFO2</a>

<a href="..\d3dkmthk\ns-d3dkmthk-_d3dkmt_createkeyedmutex2_flags.md">D3DKMT_CREATEKEYEDMUTEX2_FLAGS</a>

<a href="..\d3dukmdt\ns-d3dukmdt-_d3dddi_synchronizationobject_flags.md">D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS</a>

<a href="..\d3dkmthk\ns-d3dkmthk-_d3dkmt_createallocationflags.md">D3DKMT_CREATEALLOCATIONFLAGS</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>