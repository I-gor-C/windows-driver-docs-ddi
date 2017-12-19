---
UID: NF.wudfddi.IWDFDevice2.CreateSymbolicLinkWithReferenceString
title: IWDFDevice2::CreateSymbolicLinkWithReferenceString method
author: windows-driver-content
description: TheCreateSymbolicLinkWithReferenceString method creates a symbolic link name, and optionally, a reference string, for a device.
old-location: wdf\iwdfdevice2_createsymboliclinkwithreferencestring.htm
old-project: wdf
ms.assetid: bce932a6-2f73-4d0e-8616-45fd41abb776
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: IWDFDevice2, IWDFDevice2::CreateSymbolicLinkWithReferenceString, CreateSymbolicLinkWithReferenceString
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: IWDFDevice2.CreateSymbolicLinkWithReferenceString
req.alt-loc: WUDFx.dll
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
req.product: Windows 10 or later.
---

# IWDFDevice2::CreateSymbolicLinkWithReferenceString method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The<b>CreateSymbolicLinkWithReferenceString</b> method creates a symbolic link name, and optionally, a reference string, for a device 



## -syntax

````
HRESULT CreateSymbolicLinkWithReferenceString(
  [in]           PCWSTR pSymbolicLink,
  [in, optional] PCWSTR pReferenceString
);
````


## -parameters

### -param pSymbolicLink [in]

A pointer to a <b>NULL</b>-terminated character string that becomes the user-visible name of the device. The symbolic link name must be in the global <b>DosDevices</b> namespace.


### -param pReferenceString [in, optional]

A pointer to a <b>NULL</b>-terminated character string that Windows appends to the device name when an application uses the symbolic name that the <i>pSymbolicLink</i> parameter specifies. For more information, see the following Remarks section. This parameter is optional and can be <b>NULL</b>.


## -returns
<b>CreateSymbolicLinkWithReferenceString</b> returns S_OK if the operation succeeds. Otherwise, the method might return one of the following values:
<dl>
<dt><b>E_INVALIDARG</b></dt>
</dl>The caller specified an invalid value for an input parameter.
<dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl>The memory allocation failed.

 

This method might return one of the other values that Winerror.h contains.


## -remarks
<b>CreateSymbolicLinkWithReferenceString</b> creates a symbolic link name, and optionally a reference string, for the device that the <a href="..\wudfddi\nn-wudfddi-iwdfdevice2.md">IWDFDevice2</a> interface represents. After a driver calls <b>CreateSymbolicLinkWithReferenceString</b>, applications can use the symbolic link name to access the device.

Suppose your device's name is "\Device\MyDevice". You can create a symbolic link name of "DeviceUserName" for your device by specifying "L"DeviceUserName"" for the <i>pSymbolicLink</i> parameter. If you specify "L"Instance3"" for the <i>pReferenceString</i> parameter, you are creating a symbolic link to \Device\MyDevice\Instance3. If an application opens the device by using the symbolic link name, the I/O manager opens \Device\MyDevice and creates a WDM file object that contains the \Instance3 string as the file name. Your UMDF-based driver receives a framework-created file object, which also contains the \Instance3 string as the file name (see <a href="wdf.iwdffile_retrievefilename">IWDFFile::RetrieveFileName</a>). 

Typically, instead of providing symbolic links, framework-based drivers provide <a href="wdf.iwdfdevice_createdeviceinterface">device interfaces</a> that applications can use to access their devices.

If the device is removed unexpectedly (surprise-removed), the framework removes the symbolic link to the device. The driver can then use the symbolic link name for a new instance of the device. 

If you do not need to add a reference string to your device's symbolic link name, your driver can call <a href="wdf.iwdfdevice_createsymboliclink">IWDFDevice::CreateSymbolicLink</a> instead of <b>CreateSymbolicLinkWithReferenceString</b>.


          The following line defines a symbolic link name prefix in the global <b>DosDevices</b> namespace.
        

The following code example creates a symbolic name string, obtains the <a href="..\wudfddi\nn-wudfddi-iwdfdevice2.md">IWDFDevice2</a> interface, and then calls <b>CreateSymbolicLinkWithReferenceString</b>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
End of support

</th>
<td width="70%">
Unavailable in UMDF 2.0 and later.

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
1.9

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wudfddi\nn-wudfddi-iwdfdevice2.md">IWDFDevice2</a>
</dt>
<dt>
<a href="wdf.iwdfdevice_createsymboliclink">IWDFDevice::CreateSymbolicLink</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFDevice2::CreateSymbolicLinkWithReferenceString method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

