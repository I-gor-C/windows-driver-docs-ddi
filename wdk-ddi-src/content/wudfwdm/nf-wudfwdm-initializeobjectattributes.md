---
UID : NF:wudfwdm.InitializeObjectAttributes
title : InitializeObjectAttributes macro
author : windows-driver-content
description : The InitializeObjectAttributes macro initializes the opaque OBJECT_ATTRIBUTES structure, which specifies the properties of an object handle to routines that open handles.
old-location : kernel\initializeobjectattributes.htm
old-project : kernel
ms.assetid : ee89a9af-0bdf-476e-b4e3-eb60662e160d
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : InitializeObjectAttributes
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : macro
req.header : wudfwdm.h
req.include-header : Wdm.h, Ntddk.h, Ntdef.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : InitializeObjectAttributes
req.alt-loc : wudfwdm.h
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
req.typenames : "*PWDF_USB_REQUEST_TYPE, WDF_USB_REQUEST_TYPE"
req.product : Windows 10 or later.
---


# InitializeObjectAttributes function
The <b>InitializeObjectAttributes</b> macro initializes the opaque <a href="..\wudfwdm\ns-wudfwdm-_object_attributes.md">OBJECT_ATTRIBUTES</a> structure, which specifies the properties of an object handle to routines that open handles.

## Syntax

````
VOID InitializeObjectAttributes(
  [out]          POBJECT_ATTRIBUTES   InitializedAttributes,
  [in]           PUNICODE_STRING      ObjectName,
  [in]           ULONG                Attributes,
  [in]           HANDLE               RootDirectory,
  [in, optional] PSECURITY_DESCRIPTOR SecurityDescriptor
);
````

## Parameters

`p`



`n`



`a`



`r`



`s`




## Return Value

None

## Remarks

<b>InitializeObjectAttributes</b> initializes an <a href="..\wudfwdm\ns-wudfwdm-_object_attributes.md">OBJECT_ATTRIBUTES</a> structure that specifies the properties of an object handle to be opened. The caller can then pass a pointer to this structure to a routine that actually opens the handle. 

Driver routines that run in a process context other than that of the system process must set the OBJ_KERNEL_HANDLE flag for the <i>Attributes</i> parameter. This flag restricts the use of a handle opened for that object to processes running only in kernel mode. Otherwise, the handle can be accessed by the process in whose context the driver is running.

Note that <b>InitializeObjectAttributes</b> always sets the <b>SecurityQualityOfService</b> member of <a href="..\wudfwdm\ns-wudfwdm-_object_attributes.md">OBJECT_ATTRIBUTES</a> to <b>NULL</b>. Drivers that require a non-<b>NULL</b> value can set <b>SecurityQualityOfService</b> directly.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wudfwdm.h (include Wdm.h, Ntddk.h, Ntdef.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\wdm\nf-wdm-excreatecallback.md">ExCreateCallback</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-iocreatefile.md">IoCreateFile</a>
</dt>
<dt>
<a href="..\wudfwdm\ns-wudfwdm-_object_attributes.md">OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-pscreatesystemthread.md">PsCreateSystemThread</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs-_security_descriptor.md">SECURITY_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\wudfwdm\ns-wudfwdm-_unicode_string.md">UNICODE_STRING</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwcreatedirectoryobject.md">ZwCreateDirectoryObject</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwcreatefile.md">ZwCreateFile</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwcreatekey.md">ZwCreateKey</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwmaketemporaryobject.md">ZwMakeTemporaryObject</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwopenfile.md">ZwOpenFile</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwopenkey.md">ZwOpenKey</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwopensection.md">ZwOpenSection</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwopensymboliclinkobject.md">ZwOpenSymbolicLinkObject</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20InitializeObjectAttributes macro%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>